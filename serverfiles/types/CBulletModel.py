import json
from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass

class CBulletModel(CTypeImplBaseClass):
    m_iBulletId: int
    m_szName: str
    m_arrAttackActionIds: list[int]

    def toJSON(self):
        return json.dumps({
            "BulletId": self.m_iBulletId,
            "Name": self.m_szName,
            "AttackActionIds": self.m_arrAttackActionIds
        })