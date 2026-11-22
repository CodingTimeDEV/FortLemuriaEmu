import json

from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass

class CCharacterModel(CTypeImplBaseClass):
    m_iCharacterId: int
    m_strName: str
    m_strAnotherName: str
    m_strMkName: str
    m_iCharacterProfileId: int
    m_iModelId: int
    m_iSeqId: int
    m_strMotionListAssetName: str
    m_iIconId: int
    m_iDefaultWeaponId: int
    m_bIsPlayable: bool

    def toJSON(self) -> str:
        return json.dumps({
            "CharacterId": self.m_iCharacterId,
            "Name": self.m_strName,
            "AnotherName": self.m_strAnotherName,
            "MkName": self.m_strMkName,
            "CharacterProfileId": self.m_iCharacterProfileId,
            "ModelId": self.m_iModelId,
            "SequenceId": self.m_iSeqId,
            "MotionListAssetName": self.m_strMotionListAssetName,
            "IconId": self.m_iIconId,
            "DefaultWeaponId": self.m_iDefaultWeaponId,
            "IsPlayable": self.m_bIsPlayable
        })