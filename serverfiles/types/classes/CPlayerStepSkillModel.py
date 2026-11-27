from typing import Any
from serverfiles.types.classes.CPlayerSkillModel import CPlayerSkillModel
from serverfiles.types.enums.EMountType import EMountType
from serverfiles.types.enums.EPlayerStepSkillType import EPlayerStepSkillType

class CPlayerStepSkillModel(CPlayerSkillModel):
    m_iPlayerStepSkillId: int
    m_eMountType: EMountType
    m_ePlayerStepSkillType: EPlayerStepSkillType

    def toJSON(self) -> dict[str, Any]:
        return {
            "playerStepSkillId": self.m_iPlayerStepSkillId,
            "mountType": self.m_eMountType.value,
            "playerStepSkillType": self.m_ePlayerStepSkillType.value
        }