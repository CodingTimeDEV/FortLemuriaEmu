from enum import Enum

class EGeneralItemType(Enum):
	Undefined = 0
	Weapon = 1,
	Accessory = 2
	CharacterExp = 3
	Money = 4,
	Gold = 5,
	MountMonster = 6
	OptionMonster = 7
	GachaTicket = 8
	DevilStone = 9
	Material = 10
	LimitBreakMaterial = 11
	UpgradeMaterial = 12
	UtilityTicket = 13
	DungeonTicket = 14
	PlayableCharacter = 15
	Stamp = 16,
	EventPoint = 17
	Gift = 18,
	QuestOnlyItem = 19
	Emblem = 20,
	TradeTicket = 21
	FarmBuilding = 23
	MountMonsterEgg = 24
	ItemRecipe = 26
	FreeWalkPoint = 27