import json
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

    def toJSON(self) -> str:
        return json.dumps({
            "ItemRecipeId": self.m_iItemRecipeId,
            "Name": self.m_strName,
            "RecipeNo": self.m_iRecipeNo,
            "Rarity": self.m_eRarity.value,
            "Item": json.loads(self.m_Item.toJSON()),
            "SourceItems": [json.loads(item.toJSON()) for item in self.m_arrSourceItems]
        })