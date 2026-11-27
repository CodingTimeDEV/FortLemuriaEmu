from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class COptionMonsterAiModel(CTypeImplBaseClass):
    m_iOptionMonsterAiId: int
    m_iAiId: int
    m_iBattleRange: int
    m_iSearchRange: int
    m_iPersonalSpace: int
    m_iFOV: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "optionMonsterAiId": self.m_iOptionMonsterAiId,
            "aiId": self.m_iAiId,
            "battleRange": self.m_iBattleRange,
            "searchRange": self.m_iSearchRange,
            "personalSpace": self.m_iPersonalSpace,
            "fieldOfView": self.m_iFOV
        }