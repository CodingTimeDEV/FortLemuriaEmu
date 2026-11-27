from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EElementalType import EElementalType
from serverfiles.types.enums.EMountType import EMountType
from serverfiles.types.enums.ERarity import ERarity
from serverfiles.types.classes.CPassiveSkillTrainingModel import CPassiveSkillTrainingModel

class CPlayableCharacterModel(CTypeImplBaseClass):
    m_iPlayableCharacterId: int
    m_iCharacterId: int
    m_eRarity: ERarity
    m_eMountType: EMountType
    m_iHateId: int
    m_iExtremeSkillId: int
    m_iExtremeSkillReloadInterval: int
    m_iPlayerSkillId: int
    m_iDefaultPlayerSkillLevel: int
    m_iMinHp: int
    m_iMidHp: int
    m_iMaxHp: int
    m_iMinSp: int
    m_iMidSp: int
    m_iMaxSp: int
    m_iMinAttack: int
    m_iMidAttack: int
    m_iMaxAttack: int
    m_iMinPhysicalDefense: int
    m_iMidPhysicalDefense: int
    m_iMaxPhysicalDefense: int
    m_iMinMagicalDefense: int
    m_iMidMagicalDefense: int
    m_iMaxMagicalDefense: int
    m_eElementalType: EElementalType
    m_iMinElementalPoint: int
    m_iMidElementalPoint: int
    m_iMaxElementalPoint: int
    m_iGachaResultFaceType: int
    m_szGachaResultQuote: str
    m_bHasSpecialGachaResultPerformance: bool
    m_iLevelUpMotionClipNo: int
    m_TrainablePassiveSkills: list[CPassiveSkillTrainingModel]
    m_iCharacterShopVoiceIds: list[int]
    m_iTrainingHp: int
    m_iTrainingSp: int
    m_iTrainingAttack: int
    m_iTrainingPhysicalDefense: int
    m_iTrainingMagicalDefense: int
    m_iTrainingElementalPoint: int
    m_iFarmSkillIds: list[int]

    def toJSON(self) -> dict[str, Any]:
        return {
            "playableCharacterId": self.m_iPlayableCharacterId,
            "characterId": self.m_iCharacterId,
            "rarity": self.m_eRarity.value,
            "mountType": self.m_eMountType.value,
            "hateId": self.m_iHateId,
            "extremeSkillId": self.m_iExtremeSkillId,
            "extremeSkillReloadInterval": self.m_iExtremeSkillReloadInterval,
            "playerSkillId": self.m_iPlayerSkillId,
            "defaultPlayerSkillLevel": self.m_iDefaultPlayerSkillLevel,
            "minHp": self.m_iMinHp,
            "midHp": self.m_iMidHp,
            "maxHp": self.m_iMaxHp,
            "minSp": self.m_iMinSp,
            "midSp": self.m_iMidSp,
            "maxSp": self.m_iMaxSp,
            "minAttack": self.m_iMinAttack,
            "midAttack": self.m_iMidAttack,
            "maxAttack": self.m_iMaxAttack,
            "minPhysicalDefense": self.m_iMinPhysicalDefense,
            "midPhysicalDefense": self.m_iMidPhysicalDefense,
            "maxPhysicalDefense": self.m_iMaxPhysicalDefense,
            "minMagicalDefense": self.m_iMinMagicalDefense,
            "midMagicalDefense": self.m_iMidMagicalDefense,
            "maxMagicalDefense": self.m_iMaxMagicalDefense,
            "elementalType": self.m_eElementalType.value,
            "minElementalPoint": self.m_iMinElementalPoint,
            "midElementalPoint": self.m_iMidElementalPoint,
            "maxElementalPoint": self.m_iMaxElementalPoint,
            "gachaResultFaceType": self.m_iGachaResultFaceType,
            "gachaResultQuote": self.m_szGachaResultQuote,
            "hasSpecialGachaResultPerformance": self.m_bHasSpecialGachaResultPerformance,
            "levelUpMotionClipNo": self.m_iLevelUpMotionClipNo,
            "trainablePassiveSkills": [skill.toJSON() for skill in self.m_TrainablePassiveSkills],
            "characterShopVoiceIds": self.m_iCharacterShopVoiceIds,
            "trainingHp": self.m_iTrainingHp,
            "trainingSp": self.m_iTrainingSp,
            "trainingAttack": self.m_iTrainingAttack,
            "trainingPhysicalDefense": self.m_iTrainingPhysicalDefense,
            "trainingMagicalDefense": self.m_iTrainingMagicalDefense,
            "trainingElementalPoint": self.m_iTrainingElementalPoint,
            "farmSkillIds": self.m_iFarmSkillIds
        }