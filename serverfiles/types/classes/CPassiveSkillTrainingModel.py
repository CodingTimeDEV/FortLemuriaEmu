from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EMountType import EMountType

class CPassiveSkillTrainingModel(CTypeImplBaseClass):
    m_eMountType: EMountType
    m_iPassiveSkillId: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "mountType": self.m_eMountType.value,
            "passiveSkillId": self.m_iPassiveSkillId
        }