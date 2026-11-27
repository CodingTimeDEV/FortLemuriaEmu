"""Handlers for /api/monster-index/* endpoints."""
from serverfiles import skel

from . import register

# Req body: {}
def _monsterIndex_top(q, b):
    return {
        "commonResource":{
            "subNotifications":[],
            "badges":[
                {
                    "type": 18, "enable": False, "count": 0
                },
                {
                    "type": 19, "enable": False, "count": 0
                }
            ]
        }
    }

# Req body: {}
def mountMonster(q, b):
    return {
        "commonResource":{
                    "subNotifications":[],
                    "badges":[]
        },
        "thumbnails": [ # Array of "MonsterThumbnailModel : Model, IHasNameSortStrategyValue, IHasMonsterIndexStatus"
            {
                "indexNo": 1, # Derived
                "mountMonsterId": 1000001, # Derived
                "rarity": 1, # Derived
                "elementalType": 1, # Derived
                "mountType": 1, # Derived
                "grade": 1, # Derived
                "monsterThumbnail": {
                    "monsterId": 1000001,
                    "name": "MockMount",
                    "iconId": 1000001,
                    "monsterIndexStatus": 4,
                    "monsterModelId": 1
                }
            }
        ]
    }

# Req body: {"mountMonsterId": <long>}
def mountMonsterDetail(q, b):
    mount = skel.default("MountMonsterModel")
    mount["name"] = "MockMount"
    mount["iconId"] = 1000001
    mount["mountMonsterId"] = 1000001
    mount["indexNo"] = 1
    mount["monsterId"] = 1000001

    monster = skel.default("MonsterModel")
    monster["name"] = "MockMonster"
    monster["monsterId"] = 1000001
    monster["modelId"] = 1000001
    monster["motionId"] = 1000001
    monster["sequenceId"] = 1000001
    monster["monsterId"] = 1000001

    MonsterIndexMountMonsterDetailResponse = skel.default("MonsterIndexMountMonsterDetailResponse")
    MonsterIndexMountMonsterDetailResponse["mountMonster"] = mount
    MonsterIndexMountMonsterDetailResponse["monster"] = monster
    MonsterIndexMountMonsterDetailResponse["descriptions"] = [
        {
            "text": "Mock description",
            "iconType": 1,
            "isLocked": False
        }
    ]
    MonsterIndexMountMonsterDetailResponse["strongStatusTypes"] = [2]
    MonsterIndexMountMonsterDetailResponse["weakStatusTypes"] = [3]

    MonsterIndexMountMonsterDetailResponse["commonResource"] = {
        "subNotifications": [],
        "badges": []
    }

    return MonsterIndexMountMonsterDetailResponse

# Req body: {}
def optionMonster(q, b):
    return {
        "commonResource":{
                    "subNotifications":[],
                    "badges":[]
        },
        "thumbnails": [ # Array of "OptionMonsterThumbnailModel : Model, IHasMonsterIndexStatus, IHasSortFilterTargetModel, IHasMonsterIndexNoSortStrategyValue, IHasOptionMonsterRole, IHasElementalType"
            {
                "indexNo": 1,
                "optionMonsterId": 101001610,
                "elementalType": 1, # Derived
                "optionMonsterRole": 1, # Derived
                "monsterThumbnail": {
                    "monsterId": 101001610,
                    "name": "MockMonster",
                    "iconId": 101001610,
                    "monsterIndexStatus": 4,
                    "monsterModelId": 1
                }
            }
        ]
    }

# Req body: {"optionMonsterId": <long>}
def optionMonsterDetail(q, b):
    OptionMonsterModel = skel.default("OptionMonsterModel")
    OptionMonsterModel["optionMonsterId"] = 101001610
    OptionMonsterModel["name"] = "MockOptionMonster"
    OptionMonsterModel["indexNo"] = 1
    OptionMonsterModel["monsterId"] = 101001610
    OptionMonsterModel["iconId"] = 101001610
    OptionMonsterModel["role"] = 1

    OptionMonsterModel["scaleFactor"] = 1
    OptionMonsterModel["radius"] = 1

    MonsterModel = skel.default("MonsterModel")
    MonsterModel["name"] = "MockMonster"
    MonsterModel["monsterId"] = 101001610
    MonsterModel["modelId"] = 101001610
    MonsterModel["motionId"] = 300800110 # assets/app/external/character/enemy/animation/en_300800110_motion_list.asset
    MonsterModel["sequenceId"] = 301500111 # assets/app/external/character/enemy/sequence/en_301500111_seq_list.asset

    MonsterIndexOptionMonsterDetailResponse = skel.default("MonsterIndexOptionMonsterDetailResponse")
    MonsterIndexOptionMonsterDetailResponse["optionMonster"] = OptionMonsterModel
    MonsterIndexOptionMonsterDetailResponse["monster"] = MonsterModel
    MonsterIndexOptionMonsterDetailResponse["commonResource"] = {
        "subNotifications": [],
        "badges": []
    }

    return MonsterIndexOptionMonsterDetailResponse

register("/api/monster-index/top", _monsterIndex_top)

register("/api/monster-index/mount-monster", mountMonster)
register("/api/monster-index/mount-monster-detail", mountMonsterDetail)

register("/api/monster-index/option-monster", optionMonster)
register("/api/monster-index/option-monster-detail", optionMonsterDetail)