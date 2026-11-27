from typing import Any
from serverfiles.types.enums.ERarity import ERarity
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.classes.CPassiveSkillDetailModel import CPassiveSkillDetailModel
from serverfiles.types.classes.CPassiveSkillTriggerModel import CPassiveSkillTriggerModel

class CPassiveSkillModel(CTypeImplBaseClass):
    m_iPassiveSkillID: int
    m_szName: str
    m_eRarity: ERarity
    m_eSubRarity: ERarity
    m_iMaxLevel: int
    m_arrPassiveSkillDetailModel: list[CPassiveSkillDetailModel]
    m_arrPassiveSkillTriggerModel: list[CPassiveSkillTriggerModel]

    def toJSON(self) -> dict[str, Any]:
        return {
            "passiveSkillID": self.m_iPassiveSkillID,
            "name": self.m_szName,
            "rarity": self.m_eRarity.name,
            "subRarity": self.m_eSubRarity.name,
            "maxLevel": self.m_iMaxLevel,
            "details": [detail.toJSON() for detail in self.m_arrPassiveSkillDetailModel],
            "triggers": [trigger.toJSON() for trigger in self.m_arrPassiveSkillTriggerModel]
        }