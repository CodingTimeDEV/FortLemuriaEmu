import json
from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.EMountType import EMountType

class CPassiveSkillTrainingModel(CTypeImplBaseClass):
    m_eMountType: EMountType
    m_iPassiveSkillId: int

    def toJSON(self) -> str:
        return json.dumps({
            "MountType": self.m_eMountType.value,
            "PassiveSkillId": self.m_iPassiveSkillId
        })