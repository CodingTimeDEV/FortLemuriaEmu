from typing import Any
from serverfiles.types.enums.EQuestLabel import EQuestLabel
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

# TODO: Complete the implementation of CQuestModel
class CQuestModel(CTypeImplBaseClass):
    m_iQuestId: int
    m_szName: str
    m_szDescription: str
    m_eQuestLabel: EQuestLabel

    def toJSON(self) -> dict[str, Any]:
        return {
            "questId": self.m_iQuestId,
            "name": self.m_szName,
            "description": self.m_szDescription,
            "label": self.m_eQuestLabel.value
        }