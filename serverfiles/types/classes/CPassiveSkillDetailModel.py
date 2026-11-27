from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EPassiveSkillType import EPassiveSkillType
from serverfiles.types.enums.EPassiveSkillTargetType import EPassiveSkillTargetType

class CPassiveSkillDetailModel(CTypeImplBaseClass):
    m_ePassiveSkillType: EPassiveSkillType
    m_ePassiveSkillTargetType: EPassiveSkillTargetType
    m_iArrValues: list[int]
    m_szDescription: str
    m_szValueWithUnit: str

    def toJSON(self) -> dict[str, Any]:
        return {
            "passiveSkillType": self.m_ePassiveSkillType.value,
            "passiveSkillTargetType": self.m_ePassiveSkillTargetType.value,
            "values": self.m_iArrValues,
            "description": self.m_szDescription,
            "valueWithUnit": self.m_szValueWithUnit
        }