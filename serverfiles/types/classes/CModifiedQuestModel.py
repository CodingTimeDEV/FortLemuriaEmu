from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EQuestType import EQuestType
from serverfiles.types.classes.CQuestModel import CQuestModel

class CModifiedQuestModel(CTypeImplBaseClass):
    m_szName: str
    m_eQuestType: EQuestType
    m_Quest: CQuestModel

    def toJSON(self) -> dict[str, Any]:
        return {
            "name": self.m_szName,
            "questType": self.m_eQuestType.name,
            "quest": self.m_Quest.toJSON()
        }