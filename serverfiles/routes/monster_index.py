"""Handlers for /api/monster-index/* endpoints."""
from serverfiles import skel

from serverfiles.types.classes.CMountMonsterThumbnailModel import CMountMonsterThumbnailModel
from serverfiles.types.classes.CMonsterDescriptionModel import CMonsterDescriptionModel
from serverfiles.types.classes.CMonsterIndexMountMonsterResponse import CMonsterIndexMountMonsterResponse
from serverfiles.types.classes.COptionMonsterAiModel import COptionMonsterAiModel
from serverfiles.types.classes.CMonsterModel import CMonsterModel
from serverfiles.types.classes.CCommonResourceModel import CCommonResourceModel
from serverfiles.types.classes.CMonsterIndexOptionMonsterResponse import CMonsterIndexOptionMonsterResponse
from serverfiles.types.classes.CMonsterThumbnailModel import CMonsterThumbnailModel
from serverfiles.types.classes.COptionMonsterModel import COptionMonsterModel
from serverfiles.types.classes.COptionMonsterSkillModel import COptionMonsterSkillModel
from serverfiles.types.classes.COptionMonsterThumbnailModel import COptionMonsterThumbnailModel
from serverfiles.types.classes.CMonsterIndexOptionMonsterDetailResponse import CMonsterIndexOptionMonsterDetailResponse

from serverfiles.types.enums.EAttackType import EAttackType
from serverfiles.types.enums.EMonsterSpecies import EMonsterSpecies
from serverfiles.types.enums.EMonsterVoiceCategory import EMonsterVoiceCategory
from serverfiles.types.enums.EMonsterCategory import EMonsterCategory
from serverfiles.types.enums.EMonsterIndexStatus import EMonsterIndexStatus
from serverfiles.types.enums.EMountType import EMountType
from serverfiles.types.enums.EOptionMonsterRole import EOptionMonsterRole
from serverfiles.types.enums.EElementalType import EElementalType
from serverfiles.types.enums.ERarity import ERarity
from serverfiles.types.enums.EDeformedHeroineIconType import EDeformedHeroineIconType

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
    MountMonsterThumbnailModel: CMountMonsterThumbnailModel = CMountMonsterThumbnailModel()
    MountMonsterThumbnailModel.m_iIndexNo = 1
    MountMonsterThumbnailModel.m_iMountMonsterId = 1000001
    MountMonsterThumbnailModel.m_eRarity = ERarity(1)
    MountMonsterThumbnailModel.m_eElementalType = EElementalType(1)
    MountMonsterThumbnailModel.m_iGrade = 1
    MountMonsterThumbnailModel.m_MonsterThumbnail = CMonsterThumbnailModel()
    MountMonsterThumbnailModel.m_MonsterThumbnail.m_iMonsterId = 1000001
    MountMonsterThumbnailModel.m_MonsterThumbnail.m_szName = "MockMount"
    MountMonsterThumbnailModel.m_MonsterThumbnail.m_iIconId = 1000001
    MountMonsterThumbnailModel.m_MonsterThumbnail.m_eMonsterIndexStatus = EMonsterIndexStatus(4)
    MountMonsterThumbnailModel.m_MonsterThumbnail.m_iMonsterModelId = 1
    
    MonsterIndexMountMonsterResponse: CMonsterIndexMountMonsterResponse = CMonsterIndexMountMonsterResponse()
    MonsterIndexMountMonsterResponse.m_arrThumbnails.append(MountMonsterThumbnailModel)

    return MonsterIndexMountMonsterResponse.toJSON()

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
    monsterThumbnail = CMonsterThumbnailModel()
    monsterThumbnail.m_iMonsterId = 101001610
    monsterThumbnail.m_szName = "MockMonster"
    monsterThumbnail.m_iIconId = 101001610
    monsterThumbnail.m_eMonsterIndexStatus = EMonsterIndexStatus.Obtained
    monsterThumbnail.m_iMonsterModelId = 1

    thumbnail = COptionMonsterThumbnailModel()
    thumbnail.m_iIndexNo = 1
    thumbnail.m_iOptionMonsterId = 101001610
    thumbnail.m_eElementalType = EElementalType.Fire
    thumbnail.m_eOptionMonsterRole = EOptionMonsterRole.Attacker
    thumbnail.m_MonsterThumbnail = monsterThumbnail

    optionMonsterResponse = CMonsterIndexOptionMonsterResponse()
    optionMonsterResponse.m_arrThumbnails.append(thumbnail)

    return optionMonsterResponse.toJSON()

# Req body: {"optionMonsterId": <long>}
def optionMonsterDetail(q, b):
    OptionMonsterModel: COptionMonsterModel = COptionMonsterModel()
    OptionMonsterModel.m_iOptionMonsterId = 101001610
    OptionMonsterModel.m_szName = "MockOptionMonster"
    OptionMonsterModel.m_iIndexNo = 1
    OptionMonsterModel.m_iMonsterId = 101001610
    OptionMonsterModel.m_iIconId = 101001610
    OptionMonsterModel.m_eRarity = ERarity.Star0
    OptionMonsterModel.m_flRadius = 1
    OptionMonsterModel.m_flScaleFactor = 1
    OptionMonsterModel.m_eRole = EOptionMonsterRole.Attacker
    OptionMonsterModel.m_eElementalType = EElementalType.Fire

    MonsterModel: CMonsterModel = CMonsterModel()
    MonsterModel.m_iMonsterId = 101001610
    MonsterModel.m_szName = "MockMonster"
    MonsterModel.m_iModelId = 101001610
    MonsterModel.m_iMotionId = 300800110 # assets/app/external/character/enemy/animation/en_300800110_motion_list.asset
    MonsterModel.m_iSeqId = 301500111 # assets/app/external/character/enemy/sequence/en_301500111_seq_list.asset

    MonsterDescriptionModel: CMonsterDescriptionModel = CMonsterDescriptionModel()
    MonsterDescriptionModel.m_szText = "Mock description"
    MonsterDescriptionModel.m_bIsLocked = False

    OptionMonsterSkill: COptionMonsterSkillModel = COptionMonsterSkillModel()
    OptionMonsterSkill.m_szName = "Mock Skill"
    OptionMonsterSkill.m_szDescription = "Mock Skill Description"

    MonsterIndexOptionMonsterDetailResponse: CMonsterIndexOptionMonsterDetailResponse = CMonsterIndexOptionMonsterDetailResponse()
    MonsterIndexOptionMonsterDetailResponse.m_OptionMonster = OptionMonsterModel
    MonsterIndexOptionMonsterDetailResponse.m_Monster = MonsterModel
    MonsterIndexOptionMonsterDetailResponse.m_Description = MonsterDescriptionModel
    MonsterIndexOptionMonsterDetailResponse.m_OptionMonsterSkill = OptionMonsterSkill

    return MonsterIndexOptionMonsterDetailResponse.toJSON()

register("/api/monster-index/top", _monsterIndex_top)

register("/api/monster-index/mount-monster", mountMonster)
register("/api/monster-index/mount-monster-detail", mountMonsterDetail)

register("/api/monster-index/option-monster", optionMonster)
register("/api/monster-index/option-monster-detail", optionMonsterDetail)