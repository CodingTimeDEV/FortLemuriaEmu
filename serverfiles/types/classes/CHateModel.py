from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class CHateModel(CTypeImplBaseClass):
    m_iHateId: int
    m_szDescription: str
    m_iBasePoint: int
    m_iAttackUp: int
    m_iDebuffUp: int
    m_iHealUp: int
    m_iBuffUp: int
    m_iTimeDown: int
    m_iTargetDown: int
    m_iAttackHitDown: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "hateId": self.m_iHateId,
            "description": self.m_szDescription,
            "basePoint": self.m_iBasePoint,
            "attackUp": self.m_iAttackUp,
            "debuffUp": self.m_iDebuffUp,
            "healUp": self.m_iHealUp,
            "buffUp": self.m_iBuffUp,
            "timeDown": self.m_iTimeDown,
            "targetDown": self.m_iTargetDown,
            "attackHitDown": self.m_iAttackHitDown
        }
