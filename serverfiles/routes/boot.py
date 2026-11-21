"""Handlers for /api/boot/* endpoints."""
from ..responses import ensure_registered, account_response
from ..config import KEEP_FILE
from . import register


# ── /api/boot/registered-info ─────────────────────────────────────────────────
def _registered_info(q, b):
    ensure_registered()
    return account_response("BootRegisteredInfoResponse")


# ── /api/boot/steam-app-country ───────────────────────────────────────────────
def _steam_app_country(q, b):
    return {"country": 0}


# ── /api/boot/app-age ─────────────────────────────────────────────────────────
def _app_age(q, b):
    return {"age": 2}


# ── /api/boot/asset-bundle ────────────────────────────────────────────────────
def _asset_bundle(q, b):
    return {"assetBundleLatestHash": "0" * 32}


# ── /api/boot/top ─────────────────────────────────────────────────────────────
def _boot_top(q, b):
    from ..utils import now
    return {
        "serverTime": now(),
        "fixedDataVersion": 1,
        "fixedDataHashList": [
            {"type": t, "hash": "h%d" % t}
            for t in (1, 3, 9, 19, 20, 21, 22, 23, 24, 26, 28, 29)
        ],
    }


# ── Register ──────────────────────────────────────────────────────────────────
register("/api/boot/registered-info", _registered_info)
register("/api/boot/steam-app-country", _steam_app_country)
register("/api/boot/app-age", _app_age)
register("/api/boot/asset-bundle", _asset_bundle)
register("/api/boot/top", _boot_top)
