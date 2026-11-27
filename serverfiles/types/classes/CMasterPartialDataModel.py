from typing import Any

import msgpack
from msgpack import Timestamp
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class CMasterPartialDataModel(CTypeImplBaseClass):
    m_iId: int
    m_LastOriginalRankingQuestScheduleEndAt: Timestamp

    def toJSON(self) -> dict[str, Any]:
        return {
            "id": self.m_iId,
            "lastOriginalRankingQuestScheduleEndAt": msgpack.Timestamp(self.m_LastOriginalRankingQuestScheduleEndAt.seconds)
        }