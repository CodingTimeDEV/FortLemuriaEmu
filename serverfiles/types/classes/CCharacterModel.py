from typing import Any

from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

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

    def toJSON(self) -> dict[str, Any]:
        return {
            "characterId": self.m_iCharacterId,
            "name": self.m_strName,
            "anotherName": self.m_strAnotherName,
            "mkName": self.m_strMkName,
            "characterProfileId": self.m_iCharacterProfileId,
            "modelId": self.m_iModelId,
            "sequenceId": self.m_iSeqId,
            "motionListAssetName": self.m_strMotionListAssetName,
            "iconId": self.m_iIconId,
            "defaultWeaponId": self.m_iDefaultWeaponId,
            "isPlayable": self.m_bIsPlayable
        }