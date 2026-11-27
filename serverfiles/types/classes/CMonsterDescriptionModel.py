from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EDeformedHeroineIconType import EDeformedHeroineIconType

class CMonsterDescriptionModel(CTypeImplBaseClass):
    m_szText: str
    m_eIconType: EDeformedHeroineIconType
    m_bIsLocked: bool

    def toJSON(self) -> dict[str, Any]:
        return {
            "description": self.m_szText,
            "iconType": self.m_eIconType.name,
            "isLocked": self.m_bIsLocked
        }