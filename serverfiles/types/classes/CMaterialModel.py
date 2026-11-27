import json
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

    def toJSON(self) -> str:
        return json.dumps({
            "MaterialId": self.m_iMaterialId,
            "Name": self.m_strName,
            "Description": self.m_strDescription,
            "Rarity": self.m_eRarity.value,
            "Price": self.m_iPrice,
            "BackgroundImageType": self.m_eBackgroundImgType.value,
            "MonsterModelId": self.m_iMonsterModelId
        })