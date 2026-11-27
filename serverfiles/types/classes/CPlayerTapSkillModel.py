from typing import Any
from serverfiles.types.enums.EMountType import EMountType
from serverfiles.types.classes.CPlayerSkillModel import CPlayerSkillModel

class CPlayerTapSkillModel(CPlayerSkillModel):
    m_iPlayerTapSkillId: int
    m_iPlayerSkillId: int
    m_EMountType: EMountType
    m_iNo: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "playerTapSkillId": self.m_iPlayerTapSkillId,
            "playerSkillId": self.m_iPlayerSkillId,
            "mountType": self.m_EMountType.value,
            "no": self.m_iNo
        }