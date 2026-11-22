import json

from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.ERarity import ERarity

class CAccessoryModel(CTypeImplBaseClass):
    m_iAccessoryID: int
    m_strName: str
    m_strDescription: str
    m_eRarity: ERarity
    m_eSubRarity: ERarity
    m_iIconId: int
    m_iMonsterModelId: int
    m_iEffectId: int
    m_iPrice: int
    m_iHP: int
    m_iSP: int
    m_iAttack: int
    m_iPhysDefense: int
    m_iMagicDefense: int
    m_arrPassiveSkillIds: list[int]
    m_iPassiveSkill1Id: int
    m_iPassiveSkill2Id: int
    m_iPassiveSkill3Id: int

    def toJSON(self) -> str:
        return json.dumps({
            "AccessoryID": self.m_iAccessoryID,
            "Name": self.m_strName,
            "Description": self.m_strDescription,
            "Rarity": self.m_eRarity.value,
            "SubRarity": self.m_eSubRarity.value,
            "IconId": self.m_iIconId,
            "MonsterModelId": self.m_iMonsterModelId,
            "EffectId": self.m_iEffectId,
            "Price": self.m_iPrice,
            "Hp": self.m_iHP,
            "Sp": self.m_iSP,
            "Attack": self.m_iAttack,
            "PhysicalDefense": self.m_iPhysDefense,
            "MagicalDefense": self.m_iMagicDefense,
            "PassiveSkillIds": self.m_arrPassiveSkillIds,
            "PassiveSkill1Id": self.m_iPassiveSkill1Id,
            "PassiveSkill2Id": self.m_iPassiveSkill2Id,
            "PassiveSkill3Id": self.m_iPassiveSkill3Id
        })
