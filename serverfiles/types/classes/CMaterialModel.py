from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.ERarity import ERarity
from serverfiles.types.enums.EBackgroundImageType import EBackgroundImageType

class CMaterialModel(CTypeImplBaseClass):
    m_iMaterialId: int
    m_strName: str
    m_strDescription: str
    m_eRarity: ERarity
    m_iPrice: int
    m_eBackgroundImgType: EBackgroundImageType
    m_iMonsterModelId: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "materialId": self.m_iMaterialId,
            "name": self.m_strName,
            "description": self.m_strDescription,
            "rarity": self.m_eRarity.value,
            "price": self.m_iPrice,
            "backgroundImageType": self.m_eBackgroundImgType.value,
            "monsterModelId": self.m_iMonsterModelId
        }