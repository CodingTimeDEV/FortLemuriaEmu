import json
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.ERarity import ERarity

class CMountMonsterEggModel(CTypeImplBaseClass):
    m_iMountMonsterEggId: int
    m_strName: str
    m_eRarity: ERarity
    m_iIconId: int

    def toJSON(self) -> str:
        return json.dumps({
            "MountMonsterEggId": self.m_iMountMonsterEggId,
            "Name": self.m_strName,
            "Rarity": self.m_eRarity.value,
            "IconId": self.m_iIconId
        })