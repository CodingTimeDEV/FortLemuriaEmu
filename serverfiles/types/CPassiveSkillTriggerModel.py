import json
from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.EPassiveSkillTriggerType import EPassiveSkillTriggerType

class CPassiveSkillTriggerModel(CTypeImplBaseClass):
    m_ePassiveSkillTriggerType: EPassiveSkillTriggerType
    m_arrValues: list[int]
    m_szDescription: str

    def toJSON(self) -> str:
        return json.dumps({
            "PassiveSkillTriggerType": self.m_ePassiveSkillTriggerType.value,
            "Values": self.m_arrValues,
            "Description": self.m_szDescription
        })