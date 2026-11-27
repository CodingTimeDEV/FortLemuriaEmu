"""
Route registry.

Importing this package populates ``ROUTES`` with every handler.
Each sub-module registers its own paths via ``register()``.
"""
from typing import Callable, Dict

# route path → handler(query: str, body: dict|None) → (response, status_code)
ROUTES: Dict[str, Callable] = {}


def register(path: str, handler: Callable) -> None:
    """Register a handler for a given API path (idempotent)."""
    ROUTES[path] = handler


# ── Import every route module to trigger registration ─────────────────────────
from . import boot        # noqa: E402, F401
from . import user        # noqa: E402, F401
from . import sns         # noqa: E402, F401
from . import steam_payment  # noqa: E402, F401
from . import quest       # noqa: E402, F401
from . import farm        # noqa: E402, F401
from . import data        # noqa: E402, F401
from . import misc        # noqa: E402, F401
from . import monster_index

