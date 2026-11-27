from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EPassiveSkillTriggerType import EPassiveSkillTriggerType

class CPassiveSkillTriggerModel(CTypeImplBaseClass):
    m_ePassiveSkillTriggerType: EPassiveSkillTriggerType
    m_arrValues: list[int]
    m_szDescription: str

    def toJSON(self) -> dict[str, Any]:
        return {
            "passiveSkillTriggerType": self.m_ePassiveSkillTriggerType.value,
            "values": self.m_arrValues,
            "description": self.m_szDescription
        }