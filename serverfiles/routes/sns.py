"""Handlers for /api/sns/* endpoints."""
from .. import skel
from ..users import cur, uid, update_user, set_current_user
from . import register


def _register_steam_client(q, b):
    if cur()["steamId"] != "0":
        set_current_user(update_user(cur()["steamId"], snsSteam=True))
    d = skel.default("SnsRegisterSteamAccountWithSteamClientResponse")
    d["snsInfo"].update(userId=uid(), isRegisteredSteamAccount=True)
    return d


register("/api/sns/register-steam-account-with-steam-client", _register_steam_client)
register("/api/sns/register-steam-account", _register_steam_client)
