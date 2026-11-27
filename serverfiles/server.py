"""HTTP server: TLS-aware ThreadingHTTPServer + request dispatcher."""
import os
import re
import socket
import ssl
import time
import msgpack

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

from .config import (
    _HERE,
    CERT_FILE,
    KEY_FILE,
    HOST,
    PORT,
    SKEL_SRCDIR
)
from .auth import resolve_user
from .users import set_current_user, cur
from .utils import now, log_event
from .routes import ROUTES


# ── TLS context ────────────────────────────────────────────────────────────────
_ssl_ctx: ssl.SSLContext | None = None

try:
    _ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    _ssl_ctx.minimum_version = ssl.TLSVersion.TLSv1
    _ssl_ctx.set_ciphers("ALL:@SECLEVEL=0")
    _ssl_ctx.load_cert_chain(CERT_FILE, KEY_FILE)
except (OSError, ssl.SSLError):
    _ssl_ctx = None


# ── Handler ────────────────────────────────────────────────────────────────────
class MockHandler(BaseHTTPRequestHandler):

    def parse_request(self):
        ok = super().parse_request()
        if not ok:
            log_event({
                "t": time.strftime("%H:%M:%S"),
                "bad": self.raw_requestline[:80].hex(),
            })
        return ok

    # ── single dispatch for all verbs ─────────────────────────────────────────
    def _handle(self):
        u = urlparse(self.path)
        n = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(n) if n else b""
        dec = None
        if body:
            try:
                dec = msgpack.unpackb(body, raw=False)
            except Exception:
                dec = body[:200].hex()

        # ── log ──────────────────────────────────────────────────────────────
        log_event({
            "t": time.strftime("%H:%M:%S"),
            "m": self.command,
            "path": u.path,
            "q": u.query,
            "hdr": dict(self.headers),
            "body": dec,
        })

        # ── auth / user resolution ───────────────────────────────────────────
        ticket = None
        if u.path == "/api/steam-payment/authenticate" and isinstance(dec, dict):
            ticket = dec.get("ticket", "")

        user = resolve_user(ticket, self.headers.get("User-Token"))
        set_current_user(user)

        # ── route ────────────────────────────────────────────────────────────
        if u.path.startswith("/api/sns/login-"):
            out, code = {}, 200
        elif u.path in ROUTES:
            out, code = ROUTES[u.path](u.query, dec), 200
        else:
            out, code = self._fallback(u.path)

        # ── serialise ────────────────────────────────────────────────────────
        data = msgpack.packb(out, use_bin_type=True)
        self.send_response(code)
        self.send_header("Content-Type", "application/msgpack")
        if u.path == "/api/quest/enter" or u.path == "/api/monster-index/top":
            self.send_header("AssetBundle-Manifest", "local_latest")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("x-server-time", str(now()))
        self.send_header("Authorization", "Bearer mocktoken1234567890")
        self.send_header("user-token", (user or {}).get("token", "mocktoken1234567890"))
        self.end_headers()
        self.wfile.write(data)

    def _fallback(self, path: str):
        """
        If the path is not explicitly mocked, try to generate a default
        response from the .cs model (same behaviour as the original).
        """
        from . import skel  # local to serverfiles dir

        if not path.startswith("/api/"):
            return {"message": "not mocked", "code": 404, "type": 0}, 404

        # /api/foo/bar-baz  ->  FooBarBazResponse
        model = (
            "".join(p[:1].upper() + p[1:] for p in re.split(r"[/\-]", path[5:]))
            + "Response"
        )
        if model and os.path.exists(os.path.join(SKEL_SRCDIR, model + ".cs")):
            try:
                out = skel.default(model)
                log_event({"fallback": model})
                return out, 200
            except Exception:
                pass
        return {"message": "not mocked", "code": 404, "type": 0}, 404

    # ── verb aliases ─────────────────────────────────────────────────────────
    do_GET = do_POST = do_PUT = do_DELETE = _handle

    def log_message(self, *a):  # silence default stderr logging
        pass


# ── Server class (TLS per-connection detection) ──────────────────────────────
class MockServer(ThreadingHTTPServer):
    """Peek the first byte: 0x16 → TLS, otherwise plaintext."""

    def get_request(self):
        s, addr = super().get_request()
        if _ssl_ctx is not None:
            try:
                s.settimeout(5)
                if s.recv(1, socket.MSG_PEEK) == b"\x16":
                    s = _ssl_ctx.wrap_socket(s, server_side=True)
            except Exception as e:
                log_event({"tls_err": str(e)})
        return s, addr


def start(host: str = HOST, port: int = PORT) -> None:
    srv = MockServer((host, port), MockHandler)
    print(f"[mock-server] listening on {host}:{port} (TLS={'on' if _ssl_ctx else 'off'})")
    print(f"[mock-server] read path {_HERE}")
    
    srv.serve_forever()
