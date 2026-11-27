from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.ERarity import ERarity

class CEmblemModel(CTypeImplBaseClass):
    m_iEmblemId: int
    m_strName: str
    m_strDescription: str
    m_eRarity: ERarity
    m_iImageId: int
    m_strText: str
    m_bIsOpenConditionPublic: bool
    m_strOpenCondition: str

    def toJSON(self) -> dict[str, Any]:
        return {
            "emblemId": self.m_iEmblemId,
            "name": self.m_strName,
            "description": self.m_strDescription,
            "rarity": self.m_eRarity.value,
            "imageId": self.m_iImageId,
            "text": self.m_strText,
            "isOpenConditionPublic": self.m_bIsOpenConditionPublic,
            "openCondition": self.m_strOpenCondition
        }