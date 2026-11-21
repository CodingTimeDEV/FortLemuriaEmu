"""Authentication helpers: Steam ticket parsing & token-based lookup."""
import struct

from .users import get_or_create_user, user_by_token, _load_users


def steam_id_from_ticket(ticket: str) -> str | None:
    """
    Steam-Auth-Session-Ticket layout:
      4 B  GCToken-Länge
      8 B  Token
      8 B  SteamID64 (little-endian)
      4 B  Zeit
    """
    try:
        sid = struct.unpack_from("<Q", bytes.fromhex(ticket), 12)[0]
        if sid >> 56 == 1:
            return str(sid)
    except Exception:
        pass
    return None


def resolve_user(ticket: str | None, user_token: str | None) -> dict | None:
    """
    Determine the acting user for the current request.
    Resolution order:
      1. Steam ticket  →  get-or-create
      2. User-Token header  →  token lookup
      3. Fallback: last registered user (or None)
    """
    # 1 – Steam ticket
    if ticket:
        sid = steam_id_from_ticket(ticket)
        if sid:
            return get_or_create_user(sid)

    # 2 – User-Token header
    if user_token:
        u = user_by_token(user_token)
        if u:
            return u

    # 3 – last known user
    known = list(_load_users().values())
    return known[-1] if known else None
