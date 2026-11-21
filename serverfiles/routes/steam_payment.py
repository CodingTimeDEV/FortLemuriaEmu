"""Handlers for /api/steam-payment/* endpoints."""
from .. import skel
from ..users import uid
from . import register


def _authenticate(q, b):
    d = skel.default("SteamPaymentAuthenticateResponse")
    d["userSetting"].update(userId=uid(), isBirthday=True, enableCommunication=True)
    d["isJp"] = False
    return d


def _recover(q, b):
    return skel.default("SteamPaymentRecoverResponse")


register("/api/steam-payment/authenticate", _authenticate)
register("/api/steam-payment/recover", _recover)
