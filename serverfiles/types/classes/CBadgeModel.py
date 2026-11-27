from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EBadgeType import EBadgeType

class CBadgeModel(CTypeImplBaseClass):
    m_eType: EBadgeType
    m_bEnable: bool
    m_iCount: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "type": self.m_eType.value,
            "enable": self.m_bEnable,
            "count": self.m_iCount
        }