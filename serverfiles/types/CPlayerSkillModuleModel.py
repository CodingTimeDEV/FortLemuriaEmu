import json

from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.EPlayerSkillModuleType import EPlayerSkillModuleType

class CPlayerSkillModuleModel(CTypeImplBaseClass):
    m_ePlayerSkillModuleType: EPlayerSkillModuleType
    m_arrValues: list[int]

    def toJSON(self) -> str:
        return json.dumps({
            "PlayerSkillModuleType": self.m_ePlayerSkillModuleType.value,
            "Values": self.m_arrValues
        })