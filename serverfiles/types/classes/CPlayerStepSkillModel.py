import json
from serverfiles.types.classes.CPlayerSkillModel import CPlayerSkillModel
from serverfiles.types.enums.EMountType import EMountType
from serverfiles.types.enums.EPlayerStepSkillType import EPlayerStepSkillType

class CPlayerStepSkillModel(CPlayerSkillModel):
    m_iPlayerStepSkillId: int
    m_eMountType: EMountType
    m_ePlayerStepSkillType: EPlayerStepSkillType

    def toJSON(self) -> str:
        return json.dumps({
            "PlayerStepSkillId": self.m_iPlayerStepSkillId,
            "MountType": self.m_eMountType.value,
            "PlayerStepSkillType": self.m_ePlayerStepSkillType.value
        })