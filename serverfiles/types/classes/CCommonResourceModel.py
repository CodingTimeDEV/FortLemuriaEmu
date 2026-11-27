from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.classes.CSubNotificationModel import CSubNotificationModel
from serverfiles.types.classes.CBadgeModel import CBadgeModel


class CCommonResourceModel(CTypeImplBaseClass):
    m_SubNotifications: list[CSubNotificationModel]
    m_Badges: list[CBadgeModel]

    def toJSON(self) -> dict[str, Any]:
        return {
            "subNotifications": [sn.toJSON() for sn in self.m_SubNotifications],
            "badges": [badge.toJSON() for badge in self.m_Badges]
        }