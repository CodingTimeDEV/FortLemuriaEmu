import json
from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.ERarity import ERarity

class CEmblemModel(CTypeImplBaseClass):
    m_iEmblemId: int
    m_strName: str
    m_strDescription: str
    m_eRarity: ERarity
    m_iImageId: int
    m_strText: str
    m_bIsOpenConditionPublic: bool
    m_strOpenCondition: str

    def toJSON(self) -> str:
        return json.dumps({
            "EmblemId": self.m_iEmblemId,
            "Name": self.m_strName,
            "Description": self.m_strDescription,
            "Rarity": self.m_eRarity.value,
            "ImageId": self.m_iImageId,
            "Text": self.m_strText,
            "IsOpenConditionPublic": self.m_bIsOpenConditionPublic,
            "OpenCondition": self.m_strOpenCondition
        })