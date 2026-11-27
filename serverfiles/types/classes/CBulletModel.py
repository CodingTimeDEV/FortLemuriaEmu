from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class CBulletModel(CTypeImplBaseClass):
    m_iBulletId: int
    m_szName: str
    m_arrAttackActionIds: list[int]

    def toJSON(self) -> dict[str, Any]:
        return {
            "bulletId": self.m_iBulletId,
            "name": self.m_szName,
            "attackActionIds": self.m_arrAttackActionIds
        }