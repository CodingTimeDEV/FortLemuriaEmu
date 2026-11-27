from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EElementalType import EElementalType

class CPlayerSkillStatusModel(CTypeImplBaseClass):
    m_iPlayerSkillStatusId: int
    m_iPlayerSkillId: int
    m_iRank: int
    m_iConsumedSp: int
    m_iRecoveredSp: int
    m_iBreakPoint: int
    m_iMinBreakPoint: int
    m_iMaxBreakPoint: int
    m_iWincePoint: int
    m_iOmegaDrivePoint: int
    m_iOmegaDrivePointByWeakPoint: int
    m_iMinAttackPower: int
    m_iMaxAttackPower: int

    m_eElementalType1: EElementalType
    m_iMinElementalPower1: int
    m_iMaxElementalPower1: int

    m_eElementalType2: EElementalType
    m_iMinElementalPower2: int
    m_iMaxElementalPower2: int

    m_eElementalType3: EElementalType
    m_iMinElementalPower3: int
    m_iMaxElementalPower3: int

    m_iAttackId: int
    m_arrAttackActionIds: list[int]
    m_arrAdditionalEffectIds: list[int]
    m_arrBulletIds: list[int]

    def toJSON(self) -> dict[str, Any]:
        return {
            "statusId": self.m_iPlayerSkillStatusId,
            "playerSkillId": self.m_iPlayerSkillId,
            "rank": self.m_iRank,
            "consumedSp": self.m_iConsumedSp,
            "recoveredSp": self.m_iRecoveredSp,
            "breakPoint": self.m_iBreakPoint,
            "minBreakPoint": self.m_iMinBreakPoint,
            "maxBreakPoint": self.m_iMaxBreakPoint,
            "wincePoint": self.m_iWincePoint,
            "omegaDrivePoint": self.m_iOmegaDrivePoint,
            "omegaDrivePointByWeakPoint": self.m_iOmegaDrivePointByWeakPoint,
            "minAttackPower": self.m_iMinAttackPower,
            "maxAttackPower": self.m_iMaxAttackPower,
            "elementalType1": self.m_eElementalType1.value,
            "minElementalPower1": self.m_iMinElementalPower1,
            "maxElementalPower1": self.m_iMaxElementalPower1,
            "elementalType2": self.m_eElementalType2.value,
            "minElementalPower2": self.m_iMinElementalPower2,
            "maxElementalPower2": self.m_iMaxElementalPower2,
            "elementalType3": self.m_eElementalType3.value,
            "minElementalPower3": self.m_iMinElementalPower3,
            "maxElementalPower3": self.m_iMaxElementalPower3,
            "attackId": self.m_iAttackId,
            "attackActionIds": self.m_arrAttackActionIds,
            "additionalEffectIds": self.m_arrAdditionalEffectIds,
            "bulletIds": self.m_arrBulletIds
        }