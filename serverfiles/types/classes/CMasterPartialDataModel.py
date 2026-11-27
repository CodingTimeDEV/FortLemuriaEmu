import json

from msgpack import Timestamp
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class CMasterPartialDataModel(CTypeImplBaseClass):
    m_iId: int
    m_LastOriginalRankingQuestScheduleEndAt: Timestamp

    def toJSON(self) -> str:
        return json.dumps({
            "Id": self.m_iId,
            "LastOriginalRankingQuestScheduleEndAt": self.m_LastOriginalRankingQuestScheduleEndAt
        })