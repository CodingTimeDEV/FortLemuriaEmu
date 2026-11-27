import json
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

    def toJSON(self) -> str:
        return json.dumps({
            "PlayableCharacterId": self.m_iPlayableCharacterId,
            "CharacterId": self.m_iCharacterId,
            "Rarity": self.m_eRarity.value,
            "MountType": self.m_eMountType.value,
            "HateId": self.m_iHateId,
            "ExtremeSkillId": self.m_iExtremeSkillId,
            "ExtremeSkillReloadInterval": self.m_iExtremeSkillReloadInterval,
            "PlayerSkillId": self.m_iPlayerSkillId,
            "DefaultPlayerSkillLevel": self.m_iDefaultPlayerSkillLevel,
            "MinHp": self.m_iMinHp,
            "MidHp": self.m_iMidHp,
            "MaxHp": self.m_iMaxHp,
            "MinSp": self.m_iMinSp,
            "MidSp": self.m_iMidSp,
            "MaxSp": self.m_iMaxSp,
            "MinAttack": self.m_iMinAttack,
            "MidAttack": self.m_iMidAttack,
            "MaxAttack": self.m_iMaxAttack,
            "MinPhysicalDefense": self.m_iMinPhysicalDefense,
            "MidPhysicalDefense": self.m_iMidPhysicalDefense,
            "MaxPhysicalDefense": self.m_iMaxPhysicalDefense,
            "MinMagicalDefense": self.m_iMinMagicalDefense,
            "MidMagicalDefense": self.m_iMidMagicalDefense,
            "MaxMagicalDefense": self.m_iMaxMagicalDefense,
            "ElementalType": self.m_eElementalType.value,
            "MinElementalPoint": self.m_iMinElementalPoint,
            "MidElementalPoint": self.m_iMidElementalPoint,
            "MaxElementalPoint": self.m_iMaxElementalPoint,
            "GachaResultFaceType": self.m_iGachaResultFaceType,
            "GachaResultQuote": self.m_szGachaResultQuote,
            "HasSpecialGachaResultPerformance": self.m_bHasSpecialGachaResultPerformance,
            "LevelUpMotionClipNo": self.m_iLevelUpMotionClipNo,
            "TrainablePassiveSkills": [skill.toJSON() for skill in self.m_TrainablePassiveSkills],
            "CharacterShopVoiceIds": self.m_iCharacterShopVoiceIds,
            "TrainingHp": self.m_iTrainingHp,
            "TrainingSp": self.m_iTrainingSp,
            "TrainingAttack": self.m_iTrainingAttack,
            "TrainingPhysicalDefense": self.m_iTrainingPhysicalDefense,
            "TrainingMagicalDefense": self.m_iTrainingMagicalDefense,
            "TrainingElementalPoint": self.m_iTrainingElementalPoint,
            "FarmSkillIds": self.m_iFarmSkillIds
        })