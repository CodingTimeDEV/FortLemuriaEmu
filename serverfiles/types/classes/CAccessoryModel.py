from typing import Any

from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.ERarity import ERarity

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

    def toJSON(self) -> dict[str, Any]:
        return {
            "accessoryID": self.m_iAccessoryID,
            "name": self.m_strName,
            "description": self.m_strDescription,
            "rarity": self.m_eRarity.value,
            "subRarity": self.m_eSubRarity.value,
            "iconId": self.m_iIconId,
            "monsterModelId": self.m_iMonsterModelId,
            "effectId": self.m_iEffectId,
            "price": self.m_iPrice,
            "hp": self.m_iHP,
            "sp": self.m_iSP,
            "attack": self.m_iAttack,
            "physicalDefense": self.m_iPhysDefense,
            "magicalDefense": self.m_iMagicDefense,
            "passiveSkillIds": self.m_arrPassiveSkillIds,
            "passiveSkill1Id": self.m_iPassiveSkill1Id,
            "passiveSkill2Id": self.m_iPassiveSkill2Id,
            "passiveSkill3Id": self.m_iPassiveSkill3Id
        }
