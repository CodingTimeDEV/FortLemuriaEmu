"""Handlers for /api/data/load (the large switch on Type=N)."""
from serverfiles.types.classes.CPlayableCharacterModel import CPlayableCharacterModel

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

    d = skel.default("DataLoadResponse")
    s = d["dataSet"]

    if "Type=1&" in q:
        WeaponModel: CWeaponModel = CWeaponModel()
        WeaponModel.m_iWeaponID = 1
        WeaponModel.m_szWeaponName = "Mock Weapon"
        WeaponModel.m_szDescription = "Mock Description"
        WeaponModel.m_eWeaponType = EWeaponType.Sword
        WeaponModel.m_eWeaponUse = EWeaponUse.Default
        WeaponModel.m_eElementalType = EElementalType.Fire
        WeaponModel.m_iModelId = 220002

        DataLoadResponse.m_DataSet.m_arrWeapons.append(WeaponModel)
        d = DataLoadResponse.toJSON()

    elif "Type=3&" in q:
        MountMonsterModel: CMountMonsterModel = CMountMonsterModel()
        MountMonsterModel.m_iMountMonsterId = 1
        MountMonsterModel.m_szName = "Mock"
        MountMonsterModel.m_iMonsterId = 1
        MountMonsterModel.m_eMountType = EMountType.Strike
        MountMonsterModel.m_bIsDefault = True
        MountMonsterModel.m_iGrade = 1
        MountMonsterModel.m_iSequenceId = 1
        MountMonsterModel.m_iBaseHp = 100
        MountMonsterModel.m_iBaseSp = 100
        MountMonsterModel.m_iBaseAttack = 10
        MountMonsterModel.m_iBasePhysicalDefense = 10
        MountMonsterModel.m_iBaseMagicalDefense = 10
        MountMonsterModel.m_iHateId = 1
        MountMonsterModel.m_iPlayerSkill1Id = 1
        DataLoadResponse.m_DataSet.m_arrMountMonsterModel.append(MountMonsterModel)
        d = DataLoadResponse.toJSON()
    
    elif ("type=9" in q or "Type=9" in q or q.startswith("9")):
        PlayableCharacterModel: CPlayableCharacterModel = CPlayableCharacterModel()
        PlayableCharacterModel.m_iPlayableCharacterId = 1
        PlayableCharacterModel.m_iCharacterId = MOCK_CHARACTER_ID
        PlayableCharacterModel.m_eMountType = EMountType.Strike
        PlayableCharacterModel.m_iHateId = 1
        PlayableCharacterModel.m_iExtremeSkillId = 1
        PlayableCharacterModel.m_iPlayerSkillId = 1
        PlayableCharacterModel.m_iDefaultPlayerSkillLevel = 1
        PlayableCharacterModel.m_iMinHp = 100
        PlayableCharacterModel.m_iMidHp = 100
        PlayableCharacterModel.m_iMaxHp = 100
        PlayableCharacterModel.m_iMinSp = 100
        PlayableCharacterModel.m_iMidSp = 100
        PlayableCharacterModel.m_iMaxSp = 100
        PlayableCharacterModel.m_iMinAttack = 10
        PlayableCharacterModel.m_iMidAttack = 10
        PlayableCharacterModel.m_iMaxAttack = 10

        DataLoadResponse.m_DataSet.m_arrPlayableCharacterModel.append(PlayableCharacterModel)
        d = DataLoadResponse.toJSON()

        # pc = skel.default("PlayableCharacterModel")
        # pc.update(
        #     playableCharacterId=1,
        #     characterId=MOCK_CHARACTER_ID,
        #     rarity=1,
        #     mountType=1,
        #     playerSkillId=1,
        #     extremeSkillId=1,
        #     hateId=1,
        #     defaultPlayerSkillLevel=1,
        #     minHp=100, midHp=100, maxHp=100,
        #     minSp=100, midSp=100, maxSp=100,
        #     minAttack=10, midAttack=10, maxAttack=10,
        # )
        # s["playableCharacters"] = [pc]

    elif "Type=19&" in q:
        MonsterModel: CMonsterModel = CMonsterModel()
        MonsterModel.m_iMonsterId = 1
        MonsterModel.m_szName = "Mock"
        MonsterModel.m_iModelId = 1026002
        MonsterModel.m_iSeqId = 1
        DataLoadResponse.m_DataSet.m_arrMonsterModel.append(MonsterModel)
        d = DataLoadResponse.toJSON()

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

    elif "Type=26&" in q: # passiveSkills
        d = DataLoadResponse.toJSON()

    elif "Type=28&" in q:
        h = skel.default("HateModel")
        h.update(hateId=1, description="Mock", basePoint=100)
        s["hates"] = [h]

    elif "Type=29&" in q: # bullets
        d = DataLoadResponse.toJSON()

    return d


register("/api/data/load", _data_load)
