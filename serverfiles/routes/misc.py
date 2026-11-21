"""Miscellaneous / small endpoints that don't fit a domain module."""
from . import register

def _tip_list(q, b):
    return {"tips": [{"id": 1, "title": "mocking", "image": "", "text": "mocking"}]}


register("/api/tip/list", _tip_list)
