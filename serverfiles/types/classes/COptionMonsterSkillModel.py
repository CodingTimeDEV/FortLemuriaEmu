from typing import Any
from serverfiles.types.enums.EAttackType import EAttackType
from serverfiles.types.enums.EElementalType import EElementalType
from serverfiles.types.classes.COptionMonsterSkillStatusModel import COptionMonsterSkillStatusModel

class COptionMonsterSkillModel:
    m_iOptionMonsterSkillId: int
    m_szName: str
    m_szDescription: str
    m_eAttackType: EAttackType
    m_iRange: int
    m_arrOptionMonsterSkillStatusModel: list[COptionMonsterSkillStatusModel]
    m_iWincePoint: int
    m_eElementalType1: EElementalType
    m_eElementalType2: EElementalType
    m_eElementalType3: EElementalType
    m_iAttackId: int
    m_arrAttackActionId: list[int]
    m_arrAdditionalEffectIds: list[int]
    m_arrBulletId: list[int]
    m_arrNoVanishmentAttackIds: list[int]
    m_iBaseMaxCharge: int
    m_iBaseBreakPoint: int
    m_iBaseAttackPower: int
    m_iBaseElementalPower1: int
    m_iBaseElementalPower2: int
    m_iBaseElementalPower3: int
    m_iBaseCoolTime: int
    m_arrAdditionalEffectBaseValues: list[int]
    m_arrAdditionalEffectBaseDurations: list[int]
    m_flBaseVanishWaitTime: float

    def toJSON(self) -> dict[str, Any]:
        return {
            "optionMonsterSkillId": self.m_iOptionMonsterSkillId,
            "name": self.m_szName,
            "description": self.m_szDescription,
            "attackType": self.m_eAttackType.value,
            "range": self.m_iRange,
            "statuses": [status.toJSON() for status in self.m_arrOptionMonsterSkillStatusModel],
            "wincePoint": self.m_iWincePoint,
            "elementalType1": self.m_eElementalType1.value,
            "elementalType2": self.m_eElementalType2.value,
            "elementalType3": self.m_eElementalType3.value,
            "attackId": self.m_iAttackId,
            "attackActionIds": self.m_arrAttackActionId,
            "additionalEffectIds": self.m_arrAdditionalEffectIds,
            "bulletIds": self.m_arrBulletId,
            "noVanishmentAttackIds": self.m_arrNoVanishmentAttackIds,
            "baseMaxCharge": self.m_iBaseMaxCharge,
            "baseBreakPoint": self.m_iBaseBreakPoint,
            "baseAttackPower": self.m_iBaseAttackPower,
            "baseElementalPower1": self.m_iBaseElementalPower1,
            "baseElementalPower2": self.m_iBaseElementalPower2,
            "baseElementalPower3": self.m_iBaseElementalPower3,
            "baseCoolTime": self.m_iBaseCoolTime,
            "additionalEffectBaseValues": self.m_arrAdditionalEffectBaseValues,
            "additionalEffectBaseDurations": self.m_arrAdditionalEffectBaseDurations,
            "baseVanishWaitTime": self.m_flBaseVanishWaitTime
        }