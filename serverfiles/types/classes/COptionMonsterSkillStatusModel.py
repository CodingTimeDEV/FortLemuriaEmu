import json

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

    def toJSON(self) -> str:
        return json.dumps({
            "SkillId": self.m_iSkillId,
            "LimitBreakStep": self.m_iLimitBreakStep,
            "MaxCharge": self.m_iMaxCharge,
            "CoolTime": self.m_iCoolTime,
            "AttackPower": self.m_iAttackPower,
            "ElementalPower1": self.m_iElementalPower1,
            "ElementalPower2": self.m_iElementalPower2,
            "ElementalPower3": self.m_iElementalPower3,
            "BreakPoint": self.m_iBreakPoint,
            "VanishWaitTime": self.m_iVanishWaitTime,
            "AdditionalEffectValues": self.m_arrAdditionalEffectValues,
            "AdditionalEffectDurations": self.m_arrAdditionalEffectDurations
        })