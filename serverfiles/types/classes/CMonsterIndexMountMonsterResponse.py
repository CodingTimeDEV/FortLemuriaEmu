from typing import Any

from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.classes.CCommonResourceModel import CCommonResourceModel
from serverfiles.types.classes.CMountMonsterThumbnailModel import CMountMonsterThumbnailModel

class CMonsterIndexMountMonsterResponse(CTypeImplBaseClass):
    m_CommonResource: CCommonResourceModel
    m_arrThumbnails: list[CMountMonsterThumbnailModel]

    def toJSON(self) -> dict[str, Any]:
        return {
            "commonResource": self.m_CommonResource.toJSON() if self.m_CommonResource else None,
            "thumbnails": [thumbnail.toJSON() for thumbnail in self.m_arrThumbnails] if self.m_arrThumbnails else []
        }