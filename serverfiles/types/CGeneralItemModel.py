import json
from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.EGeneralItemType import EGeneralItemType

class CGeneralItemModel(CTypeImplBaseClass):
    m_eGeneralItemType: EGeneralItemType
    m_iId: int
    m_iCount: int
    m_strParam: str

    def toJSON(self) -> str:
        return json.dumps({
            "GeneralItemType": self.m_eGeneralItemType.value,
            "Id": self.m_iId,
            "Count": self.m_iCount,
            "Param": self.m_strParam
        })