from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.classes.CCommonResourceModel import CCommonResourceModel

class CModel(CTypeImplBaseClass):
    m_CommonResource: CCommonResourceModel

    def toJSON(self) -> dict[str, Any]:
        return {
            "commonResource": self.m_CommonResource.toJSON() if self.m_CommonResource else None
        }