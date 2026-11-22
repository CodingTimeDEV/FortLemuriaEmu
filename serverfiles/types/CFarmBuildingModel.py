import json
from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.EFarmMotionType import EFarmMotionType

class CFarmBuildingModel(CTypeImplBaseClass):
    m_iFarmBuildingId: int
    m_strName: str
    m_strDescription: str
    m_strPrefabName: str
    m_eFarmMotionType: EFarmMotionType
    m_iPreviewMountMonsterId: int
    m_iMaxLevel: int

    def toJSON(self) -> str:
        return json.dumps({
            "FarmBuildingId": self.m_iFarmBuildingId,
            "Name": self.m_strName,
            "Description": self.m_strDescription,
            "PrefabName": self.m_strPrefabName,
            "FarmMotionType": self.m_eFarmMotionType.value,
            "PreviewMountMonsterId": self.m_iPreviewMountMonsterId,
            "MaxLevel": self.m_iMaxLevel
        })