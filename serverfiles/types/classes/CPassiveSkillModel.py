import json
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

    def toJSON(self) -> str:
        return json.dumps({
            "PassiveSkillID": self.m_iPassiveSkillID,
            "Name": self.m_szName,
            "Rarity": self.m_eRarity.name,
            "SubRarity": self.m_eSubRarity.name,
            "MaxLevel": self.m_iMaxLevel,
            "Details": [detail.toJSON() for detail in self.m_arrPassiveSkillDetailModel],
            "Triggers": [trigger.toJSON() for trigger in self.m_arrPassiveSkillTriggerModel]
        })