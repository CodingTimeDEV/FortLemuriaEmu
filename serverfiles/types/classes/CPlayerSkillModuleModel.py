import json

from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EPlayerSkillModuleType import EPlayerSkillModuleType

class CPlayerSkillModuleModel(CTypeImplBaseClass):
    m_ePlayerSkillModuleType: EPlayerSkillModuleType
    m_arrValues: list[int]

    def toJSON(self) -> str:
        return json.dumps({
            "PlayerSkillModuleType": self.m_ePlayerSkillModuleType.value,
            "Values": self.m_arrValues
        })