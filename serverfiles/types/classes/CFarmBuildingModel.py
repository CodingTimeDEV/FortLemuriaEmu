from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EFarmMotionType import EFarmMotionType

class CFarmBuildingModel(CTypeImplBaseClass):
    m_iFarmBuildingId: int
    m_strName: str
    m_strDescription: str
    m_strPrefabName: str
    m_eFarmMotionType: EFarmMotionType
    m_iPreviewMountMonsterId: int
    m_iMaxLevel: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "farmBuildingId": self.m_iFarmBuildingId,
            "name": self.m_strName,
            "description": self.m_strDescription,
            "prefabName": self.m_strPrefabName,
            "farmMotionType": self.m_eFarmMotionType.value,
            "previewMountMonsterId": self.m_iPreviewMountMonsterId,
            "maxLevel": self.m_iMaxLevel
        }