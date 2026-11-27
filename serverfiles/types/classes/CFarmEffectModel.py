import json
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EFarmEffectType import EFarmEffectType
from serverfiles.types.enums.EFarmEffectTargetType import EFarmEffectTargetType

class CFarmEffectModel(CTypeImplBaseClass):
    m_eFarmEffectType: EFarmEffectType
    m_iValue: int
    m_eFarmEffectTargetType: EFarmEffectTargetType
    m_iTargetValue: int

    def toJSON(self) -> str:
        return json.dumps({
            "Type": self.m_eFarmEffectType.value,
            "Value": self.m_iValue,
            "TargetType": self.m_eFarmEffectTargetType.value,
            "TargetValue": self.m_iTargetValue
        })