from typing import Any

from serverfiles.types.enums.EMountType import EMountType
from serverfiles.types.enums.ERarity import ERarity
from serverfiles.types.enums.EElementalType import EElementalType
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class CMountMonsterModel(CTypeImplBaseClass):
	m_iMountMonsterId: int
	m_szName: str
	m_iIndexNo: int
	m_iMonsterId: int
	m_iIconId: int
	m_eRarity: ERarity
	m_eMountType: EMountType
	m_bIsDefault: bool
	m_iGrade: int
	m_iSequenceId: int
	m_iLongTapSkillId: int
	m_iBaseHp: int
	m_iBaseSp: int
	m_iBaseAttack: int
	m_iBasePhysicalDefense: int
	m_iBaseMagicalDefense: int
	m_eElementalType: EElementalType
	m_iBaseElementalPoint: int
	m_flHpLevelCoefficient: float
	m_flSpLevelCoefficient: float
	m_flAttackLevelCoefficient: float
	m_flPhysicalDefenseLevelCoefficient: float
	m_flMagicalDefenseLevelCoefficient: float
	m_flElementalPointLevelCoefficient: float
	m_flHpExpCoefficient: float
	m_flSpExpCoefficient: float
	m_flAttackExpCoefficient: float
	m_flPhysicalDefenseExpCoefficient: float
	m_flMagicalDefenseExpCoefficient: float
	m_flElementalPointExpCoefficient: float
	m_iMinTrainedHpLimit: int
	m_iMaxTrainedHpLimit: int
	m_iMinTrainedSpLimit: int
	m_iMaxTrainedSpLimit: int
	m_iMinTrainedAttackLimit: int
	m_iMaxTrainedAttackLimit: int
	m_iMinTrainedPhysicalDefenseLimit: int
	m_iMaxTrainedPhysicalDefenseLimit: int
	m_iMinTrainedMagicalDefenseLimit: int
	m_iMaxTrainedMagicalDefenseLimit: int
	m_iMinTrainedElementalPointLimit: int
	m_iMaxTrainedElementalPointLimit: int
	m_iPrice: int
	m_iHateId: int
	m_iPlayerSkill1Id: int

	def toJSON(self) -> dict[str, Any]:
		return {
			"mountMonsterId": self.m_iMountMonsterId,
			"name": self.m_szName,
			"indexNo": self.m_iIndexNo,
			"monsterId": self.m_iMonsterId,
			"iconId": self.m_iIconId,
			"rarity": self.m_eRarity.value,
			"mountType": self.m_eMountType.value,
			"isDefault": self.m_bIsDefault,
			"grade": self.m_iGrade,
			"sequenceId": self.m_iSequenceId,
			"longTapSkillId": self.m_iLongTapSkillId,
			"baseHp": self.m_iBaseHp,
			"baseSp": self.m_iBaseSp,
			"baseAttack": self.m_iBaseAttack,
			"basePhysicalDefense": self.m_iBasePhysicalDefense,
			"baseMagicalDefense": self.m_iBaseMagicalDefense,
			"elementalType": self.m_eElementalType.value,
			"baseElementalPoint": self.m_iBaseElementalPoint,
			"hpLevelCoefficient": self.m_flHpLevelCoefficient,
			"spLevelCoefficient": self.m_flSpLevelCoefficient,
			"attackLevelCoefficient": self.m_flAttackLevelCoefficient,
			"physicalDefenseLevelCoefficient": self.m_flPhysicalDefenseLevelCoefficient,
			"magicalDefenseLevelCoefficient": self.m_flMagicalDefenseLevelCoefficient,
			"elementalPointLevelCoefficient": self.m_flElementalPointLevelCoefficient,
			"hpExpCoefficient": self.m_flHpExpCoefficient,
			"spExpCoefficient": self.m_flSpExpCoefficient,
			"attackExpCoefficient": self.m_flAttackExpCoefficient,
			"physicalDefenseExpCoefficient": self.m_flPhysicalDefenseExpCoefficient,
			"magicalDefenseExpCoefficient": self.m_flMagicalDefenseExpCoefficient,
			"elementalPointExpCoefficient": self.m_flElementalPointExpCoefficient,
			"minTrainedHpLimit": self.m_iMinTrainedHpLimit,
			"maxTrainedHpLimit": self.m_iMaxTrainedHpLimit,
			"minTrainedSpLimit": self.m_iMinTrainedSpLimit,
			"maxTrainedSpLimit": self.m_iMaxTrainedSpLimit,
			"minTrainedAttackLimit": self.m_iMinTrainedAttackLimit,
			"maxTrainedAttackLimit": self.m_iMaxTrainedAttackLimit,
			"minTrainedPhysicalDefenseLimit": self.m_iMinTrainedPhysicalDefenseLimit,
			"maxTrainedPhysicalDefenseLimit": self.m_iMaxTrainedPhysicalDefenseLimit,
			"minTrainedMagicalDefenseLimit": self.m_iMinTrainedMagicalDefenseLimit,
			"maxTrainedMagicalDefenseLimit": self.m_iMaxTrainedMagicalDefenseLimit,
			"minTrainedElementalPointLimit": self.m_iMinTrainedElementalPointLimit,
			"maxTrainedElementalPointLimit": self.m_iMaxTrainedElementalPointLimit,
			"price": self.m_iPrice,
			"hateId": self.m_iHateId,
			"playerSkill1Id": self.m_iPlayerSkill1Id
		}