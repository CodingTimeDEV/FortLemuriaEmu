"""Handlers for /api/farm/* endpoints."""
from .. import skel
from ..responses import mock_user_flags, mock_character, mock_character_profile
from ..users import cur, uid, uname
from . import register

from ..config import MOCK_QUEST_MAP, MOCK_STAGE_TYPE

def _farm_top(q, b):
    d = skel.default("FarmTopResponse")
    d["userAttribute"].update(
        userId=uid(),
        userAttributeId=uid(),
        name=uname(),
        personalCode=cur()["personalCode"],
    )
    d["userFlags"] = mock_user_flags()
    d["userGeneralItemDataSet"]["currentGold"].update(
        userId=uid(), gold=0, paidGold=0, freeGold=0
    )

    m = d["mapGenerateInfo"]
    m['map'].update(mapId=MOCK_QUEST_MAP,type=MOCK_STAGE_TYPE)

    h = d["homeDataSet"]
    h.update(
        farmCharacter=mock_character(),
        farmCharacterProfile=mock_character_profile(),
        questCharacter=mock_character(),
        questCharacterProfile=mock_character_profile(),
    )
    return d


register("/api/farm/top", _farm_top)
