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
    CommonResource: CCommonResourceModel = CCommonResourceModel()
    CommonResource.m_arrSubNotifications = []
    CommonResource.m_arrBadges = []

    MountMonsterThumbnailModels: list[CMountMonsterThumbnailModel] = []
    MountMonsterThumbnailModel: CMountMonsterThumbnailModel = CMountMonsterThumbnailModel()
    MountMonsterThumbnailModel.m_iIndexNo = 1
    MountMonsterThumbnailModel.m_iMountMonsterId = 1000001
    MountMonsterThumbnailModel.m_eRarity = ERarity(1)
    MountMonsterThumbnailModel.m_eElementalType = EElementalType(1)
    MountMonsterThumbnailModel.m_eMountType = EMountType.None_
    MountMonsterThumbnailModel.m_iGrade = 1
    MountMonsterThumbnailModel.m_MonsterThumbnail = CMonsterThumbnailModel()
    MountMonsterThumbnailModel.m_MonsterThumbnail.m_iMonsterId = 1000001
    MountMonsterThumbnailModel.m_MonsterThumbnail.m_szName = "MockMount"
    MountMonsterThumbnailModel.m_MonsterThumbnail.m_iIconId = 1000001
    MountMonsterThumbnailModel.m_MonsterThumbnail.m_eMonsterIndexStatus = EMonsterIndexStatus(4)
    MountMonsterThumbnailModel.m_MonsterThumbnail.m_iMonsterModelId = 1
    MountMonsterThumbnailModels.append(MountMonsterThumbnailModel)
    
    MonsterIndexMountMonsterResponse: CMonsterIndexMountMonsterResponse = CMonsterIndexMountMonsterResponse()
    MonsterIndexMountMonsterResponse.m_CommonResource = CommonResource
    MonsterIndexMountMonsterResponse.m_arrThumbnails = MountMonsterThumbnailModels

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
    commonResource: CCommonResourceModel = CCommonResourceModel()
    commonResource.m_arrSubNotifications = []
    commonResource.m_arrBadges = []

    monsterThumbnail = CMonsterThumbnailModel()
    monsterThumbnail.m_iMonsterId = 101001610
    monsterThumbnail.m_szName = "MockMonster"
    monsterThumbnail.m_iIconId = 101001610
    monsterThumbnail.m_eMonsterIndexStatus = EMonsterIndexStatus.Obtained
    monsterThumbnail.m_iMonsterModelId = 1

    thumbnails: list[COptionMonsterThumbnailModel] = []
    thumbnail = COptionMonsterThumbnailModel()
    thumbnail.m_iIndexNo = 1
    thumbnail.m_iOptionMonsterId = 101001610
    thumbnail.m_eElementalType = EElementalType.Fire
    thumbnail.m_eOptionMonsterRole = EOptionMonsterRole.Attacker
    thumbnail.m_MonsterThumbnail = monsterThumbnail
    thumbnails.append(thumbnail)

    optionMonsterResponse = CMonsterIndexOptionMonsterResponse()
    optionMonsterResponse.m_CommonResource = commonResource
    optionMonsterResponse.m_arrThumbnails = thumbnails

    return optionMonsterResponse.toJSON()

# Req body: {"optionMonsterId": <long>}
def optionMonsterDetail(q, b):
    commonResource: CCommonResourceModel = CCommonResourceModel()
    commonResource.m_arrSubNotifications = []
    commonResource.m_arrBadges = []

    OptionMonsterAi: COptionMonsterAiModel = COptionMonsterAiModel()
    OptionMonsterAi.m_iOptionMonsterAiId = 0
    OptionMonsterAi.m_iAiId = 0
    OptionMonsterAi.m_iBattleRange = 0
    OptionMonsterAi.m_iSearchRange = 0
    OptionMonsterAi.m_iPersonalSpace = 0
    OptionMonsterAi.m_iFOV = 0

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
    OptionMonsterModel.m_iPrice = 0
    OptionMonsterModel.m_iBaseAttack = 0
    OptionMonsterModel.m_eElementalType = EElementalType.Fire
    OptionMonsterModel.m_iBaseElementalPoint = 0
    OptionMonsterModel.m_iBaseEvaluation = 0
    OptionMonsterModel.m_iOptionMonsterSkillId = 0
    OptionMonsterModel.m_iHateId = 0
    OptionMonsterModel.m_OptionMonsterAi = OptionMonsterAi

    MonsterModel: CMonsterModel = CMonsterModel()
    MonsterModel.m_iMonsterId = 101001610
    MonsterModel.m_szName = "MockMonster"
    MonsterModel.m_iEvolutionStep = 0
    MonsterModel.m_iBlowRate = 0
    MonsterModel.m_eMonsterCategory = EMonsterCategory.Normal
    MonsterModel.m_eMonsterSpecies = EMonsterSpecies.None_
    MonsterModel.m_eMonsterVoiceCategory = EMonsterVoiceCategory.None_
    MonsterModel.m_iModelId = 101001610
    MonsterModel.m_iMotionId = 300800110 # assets/app/external/character/enemy/animation/en_300800110_motion_list.asset
    MonsterModel.m_iSeqId = 301500111 # assets/app/external/character/enemy/sequence/en_301500111_seq_list.asset

    MonsterDescriptionModel: CMonsterDescriptionModel = CMonsterDescriptionModel()
    MonsterDescriptionModel.m_szText = "Mock description"
    MonsterDescriptionModel.m_eIconType = EDeformedHeroineIconType.Reserve1
    MonsterDescriptionModel.m_bIsLocked = False

    OptionMonsterSkill: COptionMonsterSkillModel = COptionMonsterSkillModel()
    OptionMonsterSkill.m_iOptionMonsterSkillId = 0
    OptionMonsterSkill.m_szName = "Mock Skill"
    OptionMonsterSkill.m_szDescription = "Mock Skill Description"
    OptionMonsterSkill.m_eAttackType = EAttackType.None_
    OptionMonsterSkill.m_iRange = 0
    OptionMonsterSkill.m_arrOptionMonsterSkillStatusModel = []
    OptionMonsterSkill.m_iWincePoint = 0
    OptionMonsterSkill.m_eElementalType1 = EElementalType.None_
    OptionMonsterSkill.m_eElementalType2 = EElementalType.None_
    OptionMonsterSkill.m_eElementalType3 = EElementalType.None_
    OptionMonsterSkill.m_iAttackId = 0
    OptionMonsterSkill.m_arrAttackActionId = []
    OptionMonsterSkill.m_arrAdditionalEffectIds = []
    OptionMonsterSkill.m_arrBulletId = []
    OptionMonsterSkill.m_arrNoVanishmentAttackIds = []
    OptionMonsterSkill.m_iBaseMaxCharge = 0
    OptionMonsterSkill.m_iBaseBreakPoint = 0
    OptionMonsterSkill.m_iBaseAttackPower = 0
    OptionMonsterSkill.m_iBaseElementalPower1 = 0
    OptionMonsterSkill.m_iBaseElementalPower2 = 0
    OptionMonsterSkill.m_iBaseElementalPower3 = 0
    OptionMonsterSkill.m_iBaseCoolTime = 0
    OptionMonsterSkill.m_arrAdditionalEffectBaseValues = []
    OptionMonsterSkill.m_arrAdditionalEffectBaseDurations = []
    OptionMonsterSkill.m_flBaseVanishWaitTime = 0.0

    MonsterIndexOptionMonsterDetailResponse: CMonsterIndexOptionMonsterDetailResponse = CMonsterIndexOptionMonsterDetailResponse()
    MonsterIndexOptionMonsterDetailResponse.m_OptionMonster = OptionMonsterModel
    MonsterIndexOptionMonsterDetailResponse.m_Monster = MonsterModel
    MonsterIndexOptionMonsterDetailResponse.m_CommonResource = commonResource
    MonsterIndexOptionMonsterDetailResponse.m_arrDropQuests = []
    MonsterIndexOptionMonsterDetailResponse.m_Description = MonsterDescriptionModel
    MonsterIndexOptionMonsterDetailResponse.m_OptionMonsterSkill = OptionMonsterSkill

    return MonsterIndexOptionMonsterDetailResponse.toJSON()

register("/api/monster-index/top", _monsterIndex_top)

register("/api/monster-index/mount-monster", mountMonster)
register("/api/monster-index/mount-monster-detail", mountMonsterDetail)

register("/api/monster-index/option-monster", optionMonster)
register("/api/monster-index/option-monster-detail", optionMonsterDetail)