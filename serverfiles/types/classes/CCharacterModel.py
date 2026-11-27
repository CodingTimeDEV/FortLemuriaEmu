from typing import Any

from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class CCharacterModel(CTypeImplBaseClass):
    m_iCharacterId: int
    m_szName: str
    m_szAnotherName: str
    m_szMkName: str
    m_iCharacterProfileId: int
    m_iModelId: int
    m_iSeqId: int
    m_szMotionListAssetName: str
    m_iIconId: int
    m_iDefaultWeaponId: int
    m_bIsPlayable: bool

    def toJSON(self) -> dict[str, Any]:
        return {
            "characterId": self.m_iCharacterId,
            "name": self.m_szName,
            "anotherName": self.m_szAnotherName,
            "mkName": self.m_szMkName,
            "characterProfileId": self.m_iCharacterProfileId,
            "modelId": self.m_iModelId,
            "sequenceId": self.m_iSeqId,
            "motionListAssetName": self.m_szMotionListAssetName,
            "iconId": self.m_iIconId,
            "defaultWeaponId": self.m_iDefaultWeaponId,
            "isPlayable": self.m_bIsPlayable
        }