"""Small helpers: time, logging, msgpack-Ext stripping."""
import json
import time
import datetime
import msgpack

from .config import LOG_FILE


def now() -> int:
    return int(time.time())


def log_event(payload: dict) -> None:
    """Append a single JSON line to the request log."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            l = json.dumps(payload, default=str, ensure_ascii=False) + "\n"
            f.write(l)
            print(l)
    except OSError:
        pass


def no_ext(x):
    """
    Recursively remove MessagePack-Ext types (Timestamp) and convert them to
    ISO-8601 strings.  The game's JsonConverter expects ISO strings instead of
    MessagePack-Ext (Timestamp) types.
    """
    if isinstance(x, dict):
        return {k: no_ext(v) for k, v in x.items()}
    if isinstance(x, list):
        return [no_ext(v) for v in x]
    if isinstance(x, msgpack.Timestamp):
        return datetime.datetime.fromtimestamp(
            x.seconds, datetime.timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
    return x
