from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.classes.CFarmEffectModel import CFarmEffectModel
from serverfiles.types.classes.CGeneralItemModel import CGeneralItemModel

class CFarmBuildingUpgradeModel(CTypeImplBaseClass):
    m_iFarmBuildingUpgradeId: int
    m_iFarmBuildingId: int
    m_iLevel: int
    m_arrFarmEffects: list[CFarmEffectModel]
    m_arrUpgradeSourceItems: list[CGeneralItemModel]

    def toJSON(self) -> dict[str, Any]:
        return {
            "farmBuildingUpgradeId": self.m_iFarmBuildingUpgradeId,
            "farmBuildingId": self.m_iFarmBuildingId,
            "level": self.m_iLevel,
            "effects": [effect.toJSON() for effect in self.m_arrFarmEffects],
            "upgradeSourceItems": [item.toJSON() for item in self.m_arrUpgradeSourceItems]
        }