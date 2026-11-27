import json
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class CQuestOnlyItemModel(CTypeImplBaseClass):
    m_iQuestOnlyItemId: int
    m_strName: str
    m_strDescription: str

    def toJSON(self) -> str:
        return json.dumps({
            "QuestOnlyItemId": self.m_iQuestOnlyItemId,
            "Name": self.m_strName,
            "Description": self.m_strDescription
        })