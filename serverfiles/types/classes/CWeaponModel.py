from typing import Any

from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.ERarity import ERarity
from serverfiles.types.enums.EWeaponType import EWeaponType
from serverfiles.types.enums.EWeaponUse import EWeaponUse
from serverfiles.types.enums.EElementalType import EElementalType

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

    def toJSON(self) -> dict[str, Any]:
        return {
            "weaponID": self.m_iWeaponID,
            "name": self.m_strWeaponName,
            "rarity": self.m_eRarity.value,
            "subRarity": self.m_eSubRarity.value,
            "description": self.m_strDescription,
            "weaponType": self.m_eWeaponType.value,
            "use": self.m_eWeaponUse.value,
            "attack": self.m_iAttackPower,
            "elementalPoint": self.m_iElementalPoint,
            "elementalType": self.m_eElementalType.value,
            "passiveSkillIds": self.m_arrPassiveSkillIds,
            "price": self.m_iPrice,
            "minPrice": self.m_iMinPrice,
            "maxPrice": self.m_iMaxPrice,
            "modelId": self.m_iModelId,
            "colorId": self.m_iColorId,
            "shaderId": self.m_iShaderId
        }