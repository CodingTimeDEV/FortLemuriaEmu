from typing import Any

from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class COptionMonsterSkillStatusModel(CTypeImplBaseClass):
    m_iSkillId: int
    m_iLimitBreakStep: int
    m_iMaxCharge: int
    m_iCoolTime: int
    m_iAttackPower: int
    m_iElementalPower1: int
    m_iElementalPower2: int
    m_iElementalPower3: int
    m_iBreakPoint: int
    m_iVanishWaitTime: float
    m_arrAdditionalEffectValues: list[int]
    m_arrAdditionalEffectDurations: list[int]

    def toJSON(self) -> dict[str, Any]:
        return {
            "skillId": self.m_iSkillId,
            "limitBreakStep": self.m_iLimitBreakStep,
            "maxCharge": self.m_iMaxCharge,
            "coolTime": self.m_iCoolTime,
            "attackPower": self.m_iAttackPower,
            "elementalPower1": self.m_iElementalPower1,
            "elementalPower2": self.m_iElementalPower2,
            "elementalPower3": self.m_iElementalPower3,
            "breakPoint": self.m_iBreakPoint,
            "vanishWaitTime": self.m_iVanishWaitTime,
            "additionalEffectValues": self.m_arrAdditionalEffectValues,
            "additionalEffectDurations": self.m_arrAdditionalEffectDurations
        }