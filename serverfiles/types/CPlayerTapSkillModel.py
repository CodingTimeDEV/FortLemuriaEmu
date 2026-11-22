import json
from serverfiles.types.EMountType import EMountType
from serverfiles.types.CPlayerSkillModel import CPlayerSkillModel

class CPlayerTapSkillModel(CPlayerSkillModel):
    m_iPlayerTapSkillId: int
    m_iPlayerSkillId: int
    m_EMountType: EMountType
    m_iNo: int

    def toJSON(self) -> str:
        return json.dumps({
            "PlayerTapSkillId": self.m_iPlayerTapSkillId,
            "PlayerSkillId": self.m_iPlayerSkillId,
            "MountType": self.m_EMountType.value,
            "No": self.m_iNo
        })