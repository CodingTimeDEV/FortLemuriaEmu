from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.ESubNotificationType import ESubNotificationType

class CSubNotificationModel(CTypeImplBaseClass):
    m_szText: str
    m_eType: ESubNotificationType
    m_NoticeAt: None  # This should likely be a datetime or timestamp type, adjust as needed
    m_szParam: str

    def toJSON(self) -> dict[str, Any]:
        return {
            "text": self.m_szText,
            "type": self.m_eType.value,
            "noticeAt": self.m_NoticeAt,
            "param": self.m_szParam
        }