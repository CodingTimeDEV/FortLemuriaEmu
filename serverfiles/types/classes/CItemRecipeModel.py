from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.ERarity import ERarity
from serverfiles.types.classes.CGeneralItemModel import CGeneralItemModel

class CItemRecipeModel(CTypeImplBaseClass):
    m_iItemRecipeId: int
    m_strName: str
    m_iRecipeNo: int
    m_eRarity: ERarity
    m_Item: CGeneralItemModel
    m_arrSourceItems: list[CGeneralItemModel]

    def toJSON(self) -> dict[str, Any]:
        return {
            "itemRecipeId": self.m_iItemRecipeId,
            "name": self.m_strName,
            "recipeNo": self.m_iRecipeNo,
            "rarity": self.m_eRarity.value,
            "item": self.m_Item.toJSON(),
            "sourceItems": [item.toJSON() for item in self.m_arrSourceItems]
        }