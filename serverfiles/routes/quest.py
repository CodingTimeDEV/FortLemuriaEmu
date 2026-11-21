"""Handlers for /api/quest/* and /api/tutorial/* endpoints."""
import json

from .. import skel
from ..config import MOCK_QUEST_MAP, MOCK_STAGE_TYPE
from ..users import uid
from ..utils import no_ext
from . import register


def _quest_enter(q, b):
    qid = (b or {}).get("questId", 1) if isinstance(b, dict) else 1
    d = skel.default("QuestEnterResponse")
    mid = MOCK_QUEST_MAP
    s = d["questStage"]
    s.update(
        questId=qid or 1,
        questName="Prologue",
        questGroupName="Prologue",
        questType=1,
        stageType=MOCK_STAGE_TYPE,
        mapType=2,
        floorCount=1,
        state=1,
        timeLimit=0,
    )
    s["enteringMap"].update(mapSceneId=mid, mapType=2)
    f = d["questCurrentFloor"]
    f.update(sceneId=mid, mapId=mid, floor=1)

    # Default start warp – MapManager uses Param.WarpId == questStage.defaultStartWarpId
    s["defaultStartWarpId"] = 1
    g = skel.default("GimmickModel")
    g.update(
        gimmickId=1,
        areaId=0,
        gimmickType=7,
        mapId=mid,
        defaultEnable=True,
        param=json.dumps(
            {
                "WarpId": 1,
                "FadeParamName": "",
                "Name": "start",
                "IsFreeWalkQuestAvailable": False,
            }
        ),
    )
    f["gimmicks"] = [g]
    return no_ext(d)


register("/api/quest/enter", _quest_enter)
register("/api/tutorial/quest-enter", _quest_enter)
