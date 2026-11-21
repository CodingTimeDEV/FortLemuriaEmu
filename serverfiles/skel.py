"""
skel – generate default msgpack-ready dicts from C# model definitions.

Public API (unchanged from the original):
    skel.default("UserModel")  →  dict
    skel.fields("UserModel")   →  list[(type, name)] | "enum" | None

New:
    Every time a type is parsed from a .cs file for the first time (cache miss),
    the result is asynchronously logged to a JSONL seed-file.  On the next
    server start the seed-file is loaded into the cache so that .cs files
    are never re-read.

    Log file location:  SKEL_CACHE_LOG env-var
                        (default: <serverfiles>/skel_cache.jsonl)
"""
from __future__ import annotations

import json
import os
import queue
import re
import threading
import time
import msgpack

from typing import Any, Dict, List, Optional, Tuple, Union

from .config import (
    SKEL_SRCDIR,
    SKEL_LOG,
)

# ── Regex ─────────────────────────────────────────────────────────────────────
FIELD_RE = re.compile(r"^\s+public ([\w<>\[\],\.]+) (\w+); //Field offset")
_ENUM_RE = re.compile(r"\bpublic\s+enum\s+(\w+)\b")

# ── C# primitive type sets ────────────────────────────────────────────────────
_INT_TYPES = frozenset({
    "int", "Int32", "long", "Int64", "short", "Int16",
    "sbyte", "byte", "Byte", "uint", "UInt32",
    "ulong", "UInt64", "ushort", "SecureInt"
})
_FLOAT_TYPES = frozenset({"float", "Single", "double", "Double"})
_VEC3 = frozenset({"Vector3", "UnityEngine.Vector3"})
_VEC2 = frozenset({"Vector2", "UnityEngine.Vector2"})


# ═══════════════════════════════════════════════════════════════════════════════
#  Async cache logger
# ═══════════════════════════════════════════════════════════════════════════════
class _AsyncCacheLogger:
    """
    Writes parsed-field entries to a JSONL file on a background thread.
    The calling thread only does a queue.put() – zero disk I/O on the hot path.
    """

    def __init__(self, log_path: str) -> None:
        self._log_path = log_path
        self._q: "queue.Queue[Optional[dict]]" = queue.Queue(maxsize=4096)
        self._thread = threading.Thread(
            target=self._worker, name="skel-cache-logger", daemon=True
        )
        self._thread.start()

    # ── public ───────────────────────────────────────────────────────────────
    def log(self, type_name: str, result: Any) -> None:
        """Enqueue one cache entry.  Non-blocking; drops if queue is full."""
        entry = {"t": int(time.time()), "type": type_name, "result": result}
        try:
            self._q.put_nowait(entry)
        except queue.Full:
            pass  # never block the request thread

    def flush(self, timeout: float = 2.0) -> None:
        """Wait until the queue is drained (useful for clean shutdown / tests)."""
        self._q.join()
        # sentinel to stop the worker
        self._q.put(None)
        self._thread.join(timeout)

    # ── worker ───────────────────────────────────────────────────────────────
    def _worker(self) -> None:
        while True:
            entry = self._q.get()
            try:
                if entry is None:
                    break
                line = json.dumps(entry, default=str, ensure_ascii=False)
                with open(self._log_path, "a", encoding="utf-8") as f:
                    f.write(line + "\n")
            except OSError:
                pass  # best-effort; never crash the server
            finally:
                self._q.task_done()

    # ── static: seed loading ────────────────────────────────────────────────
    @staticmethod
    def load_seed(log_path: str) -> Dict[str, Any]:
        """
        Read the JSONL seed-file and return {type_name: result}.
        Each line is:  {"t": <epoch>, "type": "UserModel", "result": …}
        Later entries for the same type overwrite earlier ones (last-write-wins).
        """
        seed: Dict[str, Any] = {}
        try:
            with open(log_path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                        t = entry.get("type")
                        r = entry.get("result")
                        if t and r is not None:
                            # JSON arrays → convert back to list-of-tuples
                            if isinstance(r, list) and r and isinstance(r[0], list):
                                r = [tuple(item) for item in r]
                            seed[t] = r
                    except (json.JSONDecodeError, ValueError):
                        continue
        except OSError:
            pass
        return seed


# ── Module-level instances ────────────────────────────────────────────────────
_cache: Dict[str, Any] = {}
_cache_lock = threading.Lock()
_logger = _AsyncCacheLogger(SKEL_LOG)

# Pre-populate cache from previous runs (best-effort, non-fatal)
_seed = _AsyncCacheLogger.load_seed(SKEL_LOG)
if _seed:
    with _cache_lock:
        _cache.update(_seed)


# ═══════════════════════════════════════════════════════════════════════════════
#  Public API
# ═══════════════════════════════════════════════════════════════════════════════
def cam(name: str) -> str:
    """PascalCase → camelCase."""
    return name[0].lower() + name[1:]


def fields(type_name: str) -> Union[List[Tuple[str, str]], str, None]:
    """
    Parse a .cs file and return:
      - "enum"          if the type is an enumeration
      - list of (cstype, fieldname) tuples
      - None            if the .cs file does not exist

    Result is cached; on a cache miss the .cs file is read and the result
    is asynchronously logged to the seed-file for future starts.
    """
    with _cache_lock:
        if type_name in _cache:
            return _cache[type_name]

    path = os.path.join(SKEL_SRCDIR, type_name + ".cs")
    result: Union[List[Tuple[str, str]], str, None] = None

    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            txt = f.read()

        enum_match = _ENUM_RE.search(txt)
        if enum_match and enum_match.group(1) == type_name:
            result = "enum"
        else:
            result = [
                m.groups()
                for line in txt.splitlines()
                if (m := FIELD_RE.match(line))
            ]
    else:
        print(f"[skel] file not found: {path}")

    # Async log (only on a real cache miss, not on "not found")
    if result is not None:
        with _cache_lock:
            _cache[type_name] = result
        _logger.log(type_name, result)
    else:
        print(f"[skel] cache miss: {type_name}")

    return result


def default(type_name: str, _stack: tuple = ()) -> Any:
    """
    Build a default-filled dict (or scalar) for a C# type.

    * Primitives  →  0 / 0.0 / False / "" / None
    * DateTime    →  msgpack.Timestamp (current time)
    * Vectors     →  zero-list
    * Arrays/List →  []
    * Enums       →  0
    * Structs     →  recursive dict of camelCased fields
    * Circular    →  None (cycle guard via _stack)
    """
    if type_name.startswith("Nullable<"):
        return None
    if type_name in _INT_TYPES:
        return 0
    if type_name in _FLOAT_TYPES:
        return 0.0
    if type_name == "bool":
        return False
    if type_name == "string":
        return ""
    if type_name == "DateTime":
        return msgpack.Timestamp(seconds=int(time.time()))

    if type_name in _VEC3:
        return [0.0, 0.0, 0.0]
    if type_name in _VEC2:
        return [0.0, 0.0]
    if type_name == "Quaternion":
        return [0.0, 0.0, 0.0, 1.0]
    if type_name == "Vector4":
        return [0.0, 0.0, 0.0, 0.0]

    if type_name.endswith("[]") or type_name.startswith("List<"):
        return []

    f = fields(type_name)
    if f == "enum":
        return 0
    if f is None:
        return None
    if type_name in _stack:
        return None

    out: Dict[str, Any] = {}
    for ftype, fname in f:
        out[cam(fname)] = default(ftype, _stack + (type_name,))

    return out


def clear_cache() -> None:
    """Invalidate the in-memory field cache (e.g. after .cs files change)."""
    with _cache_lock:
        _cache.clear()


def shutdown() -> None:
    """Flush the async logger and stop its thread (call on server exit)."""
    _logger.flush()


__all__ = [
    "default", "fields", "cam", "SRC",
    "clear_cache", "shutdown",
]
