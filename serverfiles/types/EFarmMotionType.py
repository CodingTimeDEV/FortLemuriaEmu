from enum import Enum

class EFarmMotionType(Enum):
	BallToss = 1
	Chasing = 2
	Frisbee = 3
	Grooming = 4
	Playing = 5
	Talking = 6
	TrainingHp = 7
	TrainingSp = 8
	TrainingAttack = 9
	TrainingPhysicalDefense = 10
	TrainingMagicalDefense = 12
	Feeding = 13
	OptionMonster = 14
	SickMonster = 15
	FreeWalk = 16
	Ride = 17
	Idle = 18
	Sit = 19