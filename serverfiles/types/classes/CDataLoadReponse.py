from typing import Any
from serverfiles.types.classes.CFixedDataSetModel import CFixedDataSetModel

class CDataLoadReponse():
    m_DataSet: CFixedDataSetModel

    def toJSON(self) -> dict[str, Any]:
        return {
            "dataSet": self.m_DataSet.toJSON()
        }