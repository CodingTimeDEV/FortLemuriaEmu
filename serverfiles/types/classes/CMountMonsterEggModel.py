from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.ERarity import ERarity

class CMountMonsterEggModel(CTypeImplBaseClass):
    m_iMountMonsterEggId: int
    m_strName: str
    m_eRarity: ERarity
    m_iIconId: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "mountMonsterEggId": self.m_iMountMonsterEggId,
            "name": self.m_strName,
            "rarity": self.m_eRarity.value,
            "iconId": self.m_iIconId
        }