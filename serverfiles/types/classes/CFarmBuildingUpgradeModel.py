import json
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.classes.CFarmEffectModel import CFarmEffectModel
from serverfiles.types.classes.CGeneralItemModel import CGeneralItemModel

class CFarmBuildingUpgradeModel(CTypeImplBaseClass):
    m_iFarmBuildingUpgradeId: int
    m_iFarmBuildingId: int
    m_iLevel: int
    m_arrFarmEffects: list[CFarmEffectModel]
    m_arrUpgradeSourceItems: list[CGeneralItemModel]

    def toJSON(self) -> str:
        return json.dumps({
            "FarmBuildingUpgradeId": self.m_iFarmBuildingUpgradeId,
            "FarmBuildingId": self.m_iFarmBuildingId,
            "Level": self.m_iLevel,
            "Effects": [effect.toJSON() for effect in self.m_arrFarmEffects],
            "UpgradeSourceItems": [item.toJSON() for item in self.m_arrUpgradeSourceItems]
        })