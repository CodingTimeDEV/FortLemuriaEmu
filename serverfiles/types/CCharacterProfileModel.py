import json

from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.EGender import EGender
from serverfiles.types.ECharacterBodyShape import ECharacterBodyShape

class CCharacterProfileModel(CTypeImplBaseClass):
    m_iCharacterProfileId: int
    m_strName: str
    m_eGender: EGender
    m_eBodyShape: ECharacterBodyShape
    m_strVoice: str
    m_iPersonality: int
    m_strAmmoName: str

    def toJSON(self) -> str:
        return json.dumps({
            "CharacterProfileId": self.m_iCharacterProfileId,
            "Name": self.m_strName,
            "Gender": self.m_eGender.name,
            "BodyShape": self.m_eBodyShape.name,
            "Voice": self.m_strVoice,
            "Personality": self.m_iPersonality,
            "AmmoName": self.m_strAmmoName
        })