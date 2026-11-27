import json
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

    def toJSON(self) -> str:
        return json.dumps({
            "HateId": self.m_iHateId,
            "Description": self.m_szDescription,
            "BasePoint": self.m_iBasePoint,
            "AttackUp": self.m_iAttackUp,
            "DebuffUp": self.m_iDebuffUp,
            "HealUp": self.m_iHealUp,
            "BuffUp": self.m_iBuffUp,
            "TimeDown": self.m_iTimeDown,
            "TargetDown": self.m_iTargetDown,
            "AttackHitDown": self.m_iAttackHitDown
        })
