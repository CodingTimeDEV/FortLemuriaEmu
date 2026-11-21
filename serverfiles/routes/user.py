"""Handlers for /api/user/* endpoints."""
from .. import skel
from ..responses import account_response
from ..users import cur, uid, update_user, set_current_user
from . import register


def _pre_register(q, b):
    return skel.default("UserPreRegisterResponse")


def _register(q, b):
    b = b if isinstance(b, dict) else {}
    s = cur()["steamId"]
    if s != "0":
        set_current_user(
            update_user(
                s,
                registered=True,
                snsSteam=True,
                name=b.get("name") or "Player%s" % uid(),
                gender=b.get("gender") or 0,
                countryCode=b.get("countryCode") or "",
            )
        )
    return account_response("UserRegisterResponse")


register("/api/user/pre-register", _pre_register)
register("/api/user/register", _register)
