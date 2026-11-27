from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class CQuestOnlyItemModel(CTypeImplBaseClass):
    m_iQuestOnlyItemId: int
    m_strName: str
    m_strDescription: str

    def toJSON(self) -> dict[str, Any]:
        return {
            "questOnlyItemId": self.m_iQuestOnlyItemId,
            "name": self.m_strName,
            "description": self.m_strDescription
        }