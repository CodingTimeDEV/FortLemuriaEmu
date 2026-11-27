import json
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

    def toJSON(self) -> str:
        return json.dumps({
            "StatusId": self.m_iPlayerSkillStatusId,
            "PlayerSkillId": self.m_iPlayerSkillId,
            "Rank": self.m_iRank,
            "ConsumedSp": self.m_iConsumedSp,
            "RecoveredSp": self.m_iRecoveredSp,
            "BreakPoint": self.m_iBreakPoint,
            "MinBreakPoint": self.m_iMinBreakPoint,
            "MaxBreakPoint": self.m_iMaxBreakPoint,
            "WincePoint": self.m_iWincePoint,
            "OmegaDrivePoint": self.m_iOmegaDrivePoint,
            "OmegaDrivePointByWeakPoint": self.m_iOmegaDrivePointByWeakPoint,
            "MinAttackPower": self.m_iMinAttackPower,
            "MaxAttackPower": self.m_iMaxAttackPower,
            "ElementalType1": self.m_eElementalType1.value,
            "MinElementalPower1": self.m_iMinElementalPower1,
            "MaxElementalPower1": self.m_iMaxElementalPower1,
            "ElementalType2": self.m_eElementalType2.value,
            "MinElementalPower2": self.m_iMinElementalPower2,
            "MaxElementalPower2": self.m_iMaxElementalPower2,
            "ElementalType3": self.m_eElementalType3.value,
            "MinElementalPower3": self.m_iMinElementalPower3,
            "MaxElementalPower3": self.m_iMaxElementalPower3,
            "AttackId": self.m_iAttackId,
            "AttackActionIds": self.m_arrAttackActionIds,
            "AdditionalEffectIds": self.m_arrAdditionalEffectIds,
            "BulletIds": self.m_arrBulletIds
        })