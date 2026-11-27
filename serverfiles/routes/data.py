"""Handlers for /api/data/load (the large switch on Type=N)."""
from .. import skel
from ..config import MOCK_CHARACTER_ID
from ..responses import mock_character, mock_character_profile
from . import register

import time
from msgpack import Timestamp

from serverfiles.types.classes.CMountMonsterModel import CMountMonsterModel
from serverfiles.types.classes.CDataLoadResponse import CDataLoadResponse
from serverfiles.types.classes.CFixedDataSetModel import CFixedDataSetModel
from serverfiles.types.classes.CWeaponModel import CWeaponModel
from serverfiles.types.classes.CMonsterModel import CMonsterModel
from serverfiles.types.classes.CMasterPartialDataModel import CMasterPartialDataModel

from serverfiles.types.enums.EMountType import EMountType
from serverfiles.types.enums.EMonsterVoiceCategory import EMonsterVoiceCategory
from serverfiles.types.enums.EMonsterSpecies import EMonsterSpecies
from serverfiles.types.enums.EMonsterCategory import EMonsterCategory
from serverfiles.types.enums.EMountType import EMountType
from serverfiles.types.enums.ERarity import ERarity
from serverfiles.types.enums.EWeaponType import EWeaponType
from serverfiles.types.enums.EWeaponUse import EWeaponUse
from serverfiles.types.enums.EElementalType import EElementalType

def _data_load(q, b):
    DataLoadResponse: CDataLoadResponse = CDataLoadResponse()
    DataLoadResponse.m_DataSet = CFixedDataSetModel()
    DataLoadResponse.m_DataSet.m_arrWeapons = []
    DataLoadResponse.m_DataSet.m_arrAccessoryModel = []
    DataLoadResponse.m_DataSet.m_arrMountMonsterModel = []
    DataLoadResponse.m_DataSet.m_arrOptionsMonsterModel = []
    DataLoadResponse.m_DataSet.m_arrMaterialModel = []
    DataLoadResponse.m_DataSet.m_arrUtilityTickets = []
    DataLoadResponse.m_DataSet.m_arrPlayableCharacterModel = []
    DataLoadResponse.m_DataSet.m_arrStampModel = []
    DataLoadResponse.m_DataSet.m_arrQuestOnlyItemModel = []
    DataLoadResponse.m_DataSet.m_arrEmblemModel = []
    DataLoadResponse.m_DataSet.m_arrMountMonsterEggModel = []
    DataLoadResponse.m_DataSet.m_arrFarmBuildingModel = []
    DataLoadResponse.m_DataSet.m_arrItemRecipeModel = []
    DataLoadResponse.m_DataSet.m_arrMonsterModel = []
    DataLoadResponse.m_DataSet.m_arrCharacterModel = []
    DataLoadResponse.m_DataSet.m_arrCharacterProfileModel = []
    DataLoadResponse.m_DataSet.m_arrPlayerSkillModel = []
    DataLoadResponse.m_DataSet.m_arrPlayerTapSkillModel = []
    DataLoadResponse.m_DataSet.m_arrPlayerStepSkillModel = []
    DataLoadResponse.m_DataSet.m_arrOptionMonsterSkillModel = []
    DataLoadResponse.m_DataSet.m_arrPassiveSkillModel = []
    DataLoadResponse.m_DataSet.m_arrFarmBuildingUpgradeModel = []
    DataLoadResponse.m_DataSet.m_arrHateModel = []
    DataLoadResponse.m_DataSet.m_arrBulletModel = []
    DataLoadResponse.m_DataSet.m_MasterPartialDataModel = CMasterPartialDataModel()
    DataLoadResponse.m_DataSet.m_MasterPartialDataModel.m_iId = 0
    DataLoadResponse.m_DataSet.m_MasterPartialDataModel.m_LastOriginalRankingQuestScheduleEndAt = Timestamp(seconds=int(time.time()))

    d = skel.default("DataLoadResponse")
    s = d["dataSet"]

    if "Type=1&" in q:
        WeaponModel: CWeaponModel = CWeaponModel()
        WeaponModel.m_iWeaponID = 1
        WeaponModel.m_szWeaponName = "Mock Weapon"
        WeaponModel.m_eRarity = ERarity.Star0
        WeaponModel.m_eSubRarity = ERarity.Star0
        WeaponModel.m_szDescription = "Mock Description"
        WeaponModel.m_eWeaponType = EWeaponType.Sword
        WeaponModel.m_eWeaponUse = EWeaponUse.Default
        WeaponModel.m_iAttackPower = 0
        WeaponModel.m_iElementalPoint = 0
        WeaponModel.m_eElementalType = EElementalType.Fire
        WeaponModel.m_arrPassiveSkillIds = []
        WeaponModel.m_iPrice = 0
        WeaponModel.m_iMinPrice = 0
        WeaponModel.m_iMaxPrice = 0
        WeaponModel.m_iModelId = 220002
        WeaponModel.m_iColorId = 0
        WeaponModel.m_iShaderId = 0

        DataLoadResponse.m_DataSet.m_arrWeapons.append(WeaponModel)
        d = DataLoadResponse.toJSON()

    elif "Type=3&" in q: # Refactor to class not working
        mm = skel.default("MountMonsterModel")
        mm.update(
            mountMonsterId=1, name="Mock", monsterId=1, rarity=1,
            mountType=1, sequenceId=1, grade=1, isDefault=True,
            hateId=1, playerSkill1Id=1,
            baseHp=100, baseSp=100, baseAttack=10,
            basePhysicalDefense=10, baseMagicalDefense=10,
        )
        s["mountMonsters"] = [mm]
    
    elif ("type=9" in q or "Type=9" in q or q.startswith("9")):
        pc = skel.default("PlayableCharacterModel")
        pc.update(
            playableCharacterId=1,
            characterId=MOCK_CHARACTER_ID,
            rarity=1,
            mountType=1,
            playerSkillId=1,
            extremeSkillId=1,
            hateId=1,
            defaultPlayerSkillLevel=1,
            minHp=100, midHp=100, maxHp=100,
            minSp=100, midSp=100, maxSp=100,
            minAttack=10, midAttack=10, maxAttack=10,
        )
        s["playableCharacters"] = [pc]

    elif "Type=19&" in q: # Refactor to class not working
        mo = skel.default("MonsterModel")
        mo.update(monsterId=1, name="Mock", modelId=1026002, sequenceId=1)
        s["monsters"] = [mo]

    elif "type=20" in q or "Type=20" in q:
        DataLoadResponse.m_DataSet.m_arrCharacterModel.append(mock_character())
        d = DataLoadResponse.toJSON()

    elif "Type=21&" in q:
        DataLoadResponse.m_DataSet.m_arrCharacterProfileModel.append(mock_character_profile())
        d = DataLoadResponse.toJSON()
        
    elif "Type=22&" in q:
        ps = skel.default("PlayerSkillModel")
        ps.update(playerSkillId=1, name="Mock", mountType=1)
        sts = skel.default("PlayerSkillStatusModel")
        sts.update(
            playerSkillStatusId=1, playerSkillId=1, rank=1,
            attackId=201, consumedSp=0, recoveredSp=0,
            wincePoint=0, omegaDrivePoint=0, omegaDrivePointByWeakPoint=0,
        )
        ps["statuses"] = [sts]
        s["playerSkills"] = [ps]

    elif "Type=23&" in q:
        pt = skel.default("PlayerTapSkillModel")
        pt.update(playerTapSkillId=1, playerSkillId=1, mountType=1, no=1)
        s["playerTapSkills"] = [pt]

    elif "Type=24&" in q:
        st = skel.default("PlayerStepSkillModel")
        st.update(playerStepSkillId=1, mountType=1, type=1, playerSkillId=1)
        s["playerStepSkills"] = [st]

    elif "Type=26&" in q:
        d = DataLoadResponse.toJSON()

    elif "Type=28&" in q:
        h = skel.default("HateModel")
        h.update(hateId=1, description="Mock", basePoint=100)
        s["hates"] = [h]

    elif "Type=29&" in q:
        d = DataLoadResponse.toJSON()

    return d


register("/api/data/load", _data_load)
