from typing import Any

from serverfiles.types.enums.EElementalType import EElementalType
from serverfiles.types.enums.EMountType import EMountType
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.ERarity import ERarity
from serverfiles.types.classes.CMonsterThumbnailModel import CMonsterThumbnailModel

class CMountMonsterThumbnailModel(CTypeImplBaseClass):
    m_iIndexNo: int
    m_iMountMonsterId: int
    m_eRarity: ERarity
    m_eElementalType: EElementalType
    m_eMountType: EMountType
    m_iGrade: int
    m_MonsterThumbnail: CMonsterThumbnailModel

    def toJSON(self) -> dict[str, Any]:
        return {
            "indexNo": self.m_iIndexNo,
            "mountMonsterId": self.m_iMountMonsterId,
            "rarity": self.m_eRarity.value,
            "elementalType": self.m_eElementalType.value,
            "mountType": self.m_eMountType.value,
            "grade": self.m_iGrade,
            "monsterThumbnail": self.m_MonsterThumbnail.toJSON() if self.m_MonsterThumbnail else None
        }