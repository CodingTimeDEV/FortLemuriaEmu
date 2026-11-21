"""User persistence: in-memory + JSON-file backed user store."""
import json
import hashlib
import threading

from .config import USERS_FILE
from .utils import now

_lock = threading.Lock()
_cur = threading.local()  # thread-local acting user


# ── File I/O ───────────────────────────────────────────────────────────────────
def _load_users() -> dict:
    try:
        return json.load(open(USERS_FILE, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _save_users(u: dict) -> None:
    json.dump(u, open(USERS_FILE, "w", encoding="utf-8"), indent=1)


# ── CRUD ───────────────────────────────────────────────────────────────────────
def get_or_create_user(steam_id: str) -> dict:
    with _lock:
        users = _load_users()
        u = users.get(steam_id)
        if u is None:
            n = max([int(x["userId"]) for x in users.values()] + [0]) + 1
            u = {
                "steamId": steam_id,
                "userId": str(n),
                "name": "",
                "personalCode": "%08d" % n,
                "registered": False,
                "snsSteam": False,
                "gender": 0,
                "countryCode": "",
                "created": now(),
                "token": hashlib.sha256(
                    ("volzerk-mock" + steam_id).encode()
                ).hexdigest()[:32],
            }
            users[steam_id] = u
            _save_users(users)
        return dict(u)


def update_user(steam_id: str, **kw) -> dict:
    with _lock:
        users = _load_users()
        users[steam_id].update(kw)
        _save_users(users)
        return dict(users[steam_id])


def user_by_token(tok: str) -> dict | None:
    for u in _load_users().values():
        if u["token"] == tok:
            return u
    return None


# ── Thread-local acting user ──────────────────────────────────────────────────
def set_current_user(user: dict | None) -> None:
    _cur.user = user


def cur() -> dict:
    """Return the thread-local user or a safe default."""
    return (
        getattr(_cur, "user", None)
        or {
            "steamId": "0",
            "userId": "1",
            "name": "Mock",
            "personalCode": "00000001",
            "registered": True,
            "snsSteam": True,
        }
    )


def uid() -> str:
    return cur()["userId"]


def uname() -> str:
    return cur()["name"] or "Player%s" % cur()["userId"]
