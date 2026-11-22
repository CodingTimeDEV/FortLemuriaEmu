from enum import Enum

class EFarmEffectType(Enum):
	ExpHP = 2
	ExpAttack = 3
	ExpPhysicalDefense = 4
	ExpMagicalDefense = 6
	ExpElement = 7
	ExpSP = 8
	Love = 9,
	Tension = 10
	Fullness = 11
	OptionMonsterExp = 12
	TrainingBuildingDamageDecrease = 13
	SubElementalPointFire = 15
	SubElementalPointWind = 16
	SubElementalPointThunder = 17
	SubElementalPointWater = 18
	SubElementalPointLight = 19
	SubElementalPointDark = 20
	OptionMonsterPresentFarmMaterial = 21
	OptionMonsterPresentFarmFeed = 22
	OptionMonsterPresentUpgradeMaterial = 23
	MountMonsterPresentItemPercentage = 24
	MountMonsterDiseasePercentage = 25
	TrainingBuildingAddValue = 26