from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EMonsterIndexStatus import EMonsterIndexStatus

class CMonsterThumbnailModel(CTypeImplBaseClass):
    m_iMonsterId: int
    m_szName: str
    m_iIconId: int
    m_eMonsterIndexStatus: EMonsterIndexStatus
    m_iMonsterModelId: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "monsterId": self.m_iMonsterId,
            "name": self.m_szName,
            "iconId": self.m_iIconId,
            "monsterIndexStatus": self.m_eMonsterIndexStatus.value,
            "monsterModelId": self.m_iMonsterModelId
        }