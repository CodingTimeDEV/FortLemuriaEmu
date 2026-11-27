from typing import Any
from serverfiles.types.classes.CFixedDataSetModel import CFixedDataSetModel
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class CDataLoadResponse(CTypeImplBaseClass  ):
    m_DataSet: CFixedDataSetModel

    def toJSON(self) -> dict[str, Any]:
        return {
            "dataSet": self.m_DataSet.toJSON()
        }