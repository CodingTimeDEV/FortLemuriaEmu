import json
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class COptionMonsterAiModel(CTypeImplBaseClass):
    m_iOptionMonsterAiId: int
    m_iAiId: int
    m_iBattleRange: int
    m_iSearchRange: int
    m_iPersonalSpace: int
    m_iFOV: int

    def toJSON(self) -> str:
        return json.dumps({
            "OptionMonsterAiId": self.m_iOptionMonsterAiId,
            "AiId": self.m_iAiId,
            "BattleRange": self.m_iBattleRange,
            "SearchRange": self.m_iSearchRange,
            "PersonalSpace": self.m_iPersonalSpace,
            "FieldOfView": self.m_iFOV
        })