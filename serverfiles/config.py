"""Central configuration: paths, env-var flags, constants."""
import os

# ── Paths ──────────────────────────────────────────────────────────────────────
_HERE = os.path.dirname(os.path.abspath(__file__))
_SERVERFILES = os.path.dirname(_HERE)  # …/serverfiles
LOG_FILE = os.path.join(_SERVERFILES, "mock_requests.log")
USERS_FILE = os.path.join(_SERVERFILES, "users.json")
KEEP_FILE = os.path.join(_SERVERFILES, "keep.txt")
CERT_FILE = r".\cert.pem"
KEY_FILE = r".\key.pem"
SKEL_SRCDIR = r"C:\Users\philip.asx\.copilot\session-state\f9a4d511-0953-49d3-8496-bf546748c091\files\diff\DiffableCs\Database\Ammo"
SKEL_LOG = os.path.join(_SERVERFILES, "skel_cache.json")

# ── Env-var switches ───────────────────────────────────────────────────────────
SKIP_PROLOGUE: bool = os.environ.get("MOCK_SKIP_PROLOGUE", "1") == "1"
MOCK_CHARACTER_ID: int = int(os.environ.get("MOCK_CHARACTER_ID", "1001"))
MOCK_CUR_QUEST: int = int(os.environ.get("MOCK_CUR_QUEST", "-1"))
MOCK_QUEST_MAP: int = int(os.environ.get("MOCK_QUEST_MAP", "10100101101"))
MOCK_STAGE_TYPE: int = int(os.environ.get("MOCK_STAGE_TYPE", "1"))

# ── Server ─────────────────────────────────────────────────────────────────────
HOST = "127.0.0.1"
PORT = 8092
