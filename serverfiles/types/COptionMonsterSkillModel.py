import json
from serverfiles.types.EAttackType import EAttackType
from serverfiles.types.EElementalType import EElementalType
from serverfiles.types.COptionMonsterSkillStatusModel import COptionMonsterSkillStatusModel

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

    def toJSON(self) -> str:
        return json.dumps({
            "OptionMonsterSkillId": self.m_iOptionMonsterSkillId,
            "Name": self.m_szName,
            "Description": self.m_szDescription,
            "AttackType": self.m_eAttackType.value,
            "Range": self.m_iRange,
            "Statuses": [status.toJSON() for status in self.m_arrOptionMonsterSkillStatusModel],
            "WincePoint": self.m_iWincePoint,
            "ElementalType1": self.m_eElementalType1.value,
            "ElementalType2": self.m_eElementalType2.value,
            "ElementalType3": self.m_eElementalType3.value,
            "AttackId": self.m_iAttackId,
            "AttackActionIds": self.m_arrAttackActionId,
            "AdditionalEffectIds": self.m_arrAdditionalEffectIds,
            "BulletIds": self.m_arrBulletId,
            "NoVanishmentAttackIds": self.m_arrNoVanishmentAttackIds,
            "BaseMaxCharge": self.m_iBaseMaxCharge,
            "BaseBreakPoint": self.m_iBaseBreakPoint,
            "BaseAttackPower": self.m_iBaseAttackPower,
            "BaseElementalPower1": self.m_iBaseElementalPower1,
            "BaseElementalPower2": self.m_iBaseElementalPower2,
            "BaseElementalPower3": self.m_iBaseElementalPower3,
            "BaseCoolTime": self.m_iBaseCoolTime,
            "AdditionalEffectBaseValues": self.m_arrAdditionalEffectBaseValues,
            "AdditionalEffectBaseDurations": self.m_arrAdditionalEffectBaseDurations,
            "BaseVanishWaitTime": self.m_flBaseVanishWaitTime
        })