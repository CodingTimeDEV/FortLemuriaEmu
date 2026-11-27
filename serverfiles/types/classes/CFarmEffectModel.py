from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EFarmEffectType import EFarmEffectType
from serverfiles.types.enums.EFarmEffectTargetType import EFarmEffectTargetType

class CFarmEffectModel(CTypeImplBaseClass):
    m_eFarmEffectType: EFarmEffectType
    m_iValue: int
    m_eFarmEffectTargetType: EFarmEffectTargetType
    m_iTargetValue: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "type": self.m_eFarmEffectType.value,
            "value": self.m_iValue,
            "targetType": self.m_eFarmEffectTargetType.value,
            "targetValue": self.m_iTargetValue
        }