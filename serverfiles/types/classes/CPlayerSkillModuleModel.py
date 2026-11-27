from typing import Any

from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EPlayerSkillModuleType import EPlayerSkillModuleType

class CPlayerSkillModuleModel(CTypeImplBaseClass):
    m_ePlayerSkillModuleType: EPlayerSkillModuleType
    m_arrValues: list[int]

    def toJSON(self) -> dict[str, Any]:
        return {
            "playerSkillModuleType": self.m_ePlayerSkillModuleType.value,
            "values": self.m_arrValues
        }