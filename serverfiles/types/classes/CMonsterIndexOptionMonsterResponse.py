from typing import Any

from serverfiles.types.classes.CModel import CModel
from serverfiles.types.classes.COptionMonsterThumbnailModel import COptionMonsterThumbnailModel

class CMonsterIndexOptionMonsterResponse(CModel):
    m_Thumbnails: list[COptionMonsterThumbnailModel]

    def toJSON(self) -> dict[str, Any]:
        return {
            "thumbnails": [thumbnail.toJSON() for thumbnail in self.m_Thumbnails]
        }