from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EGeneralItemType import EGeneralItemType

class CGeneralItemModel(CTypeImplBaseClass):
    m_eGeneralItemType: EGeneralItemType
    m_iId: int
    m_iCount: int
    m_strParam: str

    def toJSON(self) -> dict[str, Any]:
        return {
            "generalItemType": self.m_eGeneralItemType.value,
            "id": self.m_iId,
            "count": self.m_iCount,
            "param": self.m_strParam
        }