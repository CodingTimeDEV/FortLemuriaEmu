import json
from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass

class CStampModel(CTypeImplBaseClass):
    m_iStampId: int
    m_strName: str
    m_strDescription: str
    m_strText: str
    m_strImage: str
    m_strSeName: str

    def toJSON(self) -> str:
        return json.dumps({
            "StampId": self.m_iStampId,
            "Name": self.m_strName,
            "Description": self.m_strDescription,
            "Text": self.m_strText,
            "Image": self.m_strImage,
            "SeName": self.m_strSeName
        })
    