from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.classes.CMonsterThumbnailModel import CMonsterThumbnailModel
from serverfiles.types.enums.EElementalType import EElementalType
from serverfiles.types.enums.EOptionMonsterRole import EOptionMonsterRole

class COptionMonsterThumbnailModel(CTypeImplBaseClass):
    m_iIndexNo: int
    m_iOptionMonsterId: int
    m_eElementalType: EElementalType
    m_eOptionMonsterRole: EOptionMonsterRole
    m_MonsterThumbnail: CMonsterThumbnailModel

    def toJSON(self) -> dict[str, Any]:
        return {
            "indexNo": self.m_iIndexNo,
            "optionMonsterId": self.m_iOptionMonsterId,
            "elementalType": self.m_eElementalType.value,
            "optionMonsterRole": self.m_eOptionMonsterRole.value,
            "monsterThumbnail": self.m_MonsterThumbnail.toJSON()
        }
