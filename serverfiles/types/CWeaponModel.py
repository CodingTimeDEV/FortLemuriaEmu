import json

from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.ERarity import ERarity
from serverfiles.types.EWeaponType import EWeaponType
from serverfiles.types.EWeaponUse import EWeaponUse
from serverfiles.types.EElementalType import EElementalType

class CWeaponModel(CTypeImplBaseClass):
    m_iWeaponID: int
    m_strWeaponName: str
    m_eRarity: ERarity
    m_eSubRarity: ERarity
    m_strDescription: str
    m_eWeaponType: EWeaponType
    m_eWeaponUse: EWeaponUse
    m_iAttackPower: int
    m_iElementalPoint: int
    m_eElementalType: EElementalType
    m_arrPassiveSkillIds: list[int]
    m_iPrice: int
    m_iMinPrice: int
    m_iMaxPrice: int
    m_iModelId: int
    m_iColorId: int
    m_iShaderId: int

    def toJSON(self) -> str:
        return json.dumps({
            "WeaponID": self.m_iWeaponID,
            "Name": self.m_strWeaponName,
            "Rarity": self.m_eRarity.value,
            "SubRarity": self.m_eSubRarity.value,
            "Description": self.m_strDescription,
            "WeaponType": self.m_eWeaponType.value,
            "Use": self.m_eWeaponUse.value,
            "Attack": self.m_iAttackPower,
            "ElementalPoint": self.m_iElementalPoint,
            "ElementalType": self.m_eElementalType.value,
            "PassiveSkillIds": self.m_arrPassiveSkillIds,
            "Price": self.m_iPrice,
            "MinPrice": self.m_iMinPrice,
            "MaxPrice": self.m_iMaxPrice,
            "ModelId": self.m_iModelId,
            "ColorId": self.m_iColorId,
            "ShaderId": self.m_iShaderId
        })