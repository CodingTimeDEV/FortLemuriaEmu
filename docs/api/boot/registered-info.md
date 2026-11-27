# Endpoint: `/api/boot/registered-info`

* **Status:** 🟡 Mock / Skeleton
* **Category:** Boot / Auth
* **Related Game Classes (Cpp2IL):** Req: BootRegisteredInfoRequest ; Resp: BootRegisteredInfoResponse
---

## 📋 Overview
<!-- Briefly explain when the client calls this endpoint and what it is used for (e.g., "Called right after loading into the Home Farm to fetch spawned NPCs and daily rewards."). -->
Called at game startup, right after initial data init / loading.
Probably used to check if user is registered and gather user data.

---

## 📥 Request (Client ➔ Server)

### Headers (if special)
```http
"Accept": "application/msgpack", 
"Accept-Encoding": "gzip", 
"User-Agent": [...], 
"Content-Type": "application/msgpack", 
"Idempotency-Key": "<KEY>", 
"Authorization": "Bearer mocktoken1234567890", 
"AssetBundle-Manifest": "local_latest", 
"User-Token": "mocktoken1234567890", 
"lang": "1", 
"Fixed-Data-Version": "1", 
"Host": "127.0.0.1:8092", 
"Connection": "Keep-Alive, TE", 
"TE": "identity", 
"Content-Length": "14"
```

### Payload Structure
```json
{
  "steamClient": true
}
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `steamClient` | `bool` | Yes | Wether connecting user is a steam user |

---

## 📤 Response (Server ➔ Client)

### Expected JSON Structure
```json
{
    "userDataSet": {
        "userAttribute": {
            "userId": "1", 
            "userAttributeId": "1", 
            "personalCode": "00000001", 
            "name": "Player1", 
            "message": "", 
            "gender": 0, 
            "mainUserCharacterId": "", 
            "money": 0, 
            "maxWeaponNum": 0, 
            "maxAccessoryNum": 0, 
            "maxMountMonsterNum": 0, 
            "maxOptionMonsterNum": 0, 
            "characterExp": 0, 
            "freeWalkPoint": 0, 
            "mountMonsterDeckNo": 0, 
            "currentPartyNo": 1, 
            "userProgressContents": [], 
            "mapType": 0, 
            "mapId": 0, 
            "dungeonId": 0, 
            "bossDropBonusExpireAt": {"seconds": 1795360675, "nanoseconds": 0}, 
            "wasBossDropBonusEnableAsLastDungeonEnter": false, 
            "characterThumbnail": {
                "characterIconId": 0, 
                "rarity": 0, 
                "mountType": 0, 
                "elementalType": 0
            }, 
            "emblem": {
                "emblemId": 0, 
                "name": "", 
                "description": "", 
                "rarity": 0, 
                "imageId": 0, 
                "text": "", 
                "isOpenConditionPublic": false, 
                "openCondition": ""
            }, 
            "privacySettings": 0, 
            "canTrackAd": false
        }, 
        "userCurrentQuest": {
            "userId": "1", 
            "selectedDifficulty": 0, 
            "ranks": [], 
            "questId": 0, 
            "floor": 0, 
            "acceptedAt": {"seconds": 1795360675, "nanoseconds": 0}, 
            "roomId": ""
        }, 
        "userGeneralItemDataSet": {
            "userAttribute": {
                "userId": "", 
                "userAttributeId": "", 
                "personalCode": "", 
                "name": "", 
                "message": "", 
                "gender": 0, 
                "mainUserCharacterId": "", 
                "money": 0, 
                "maxWeaponNum": 0, 
                "maxAccessoryNum": 0, 
                "maxMountMonsterNum": 0, 
                "maxOptionMonsterNum": 0, 
                "characterExp": 0, 
                "freeWalkPoint": 0, 
                "mountMonsterDeckNo": 0, 
                "currentPartyNo": 0, 
                "userProgressContents": [], 
                "mapType": 0, 
                "mapId": 0, 
                "dungeonId": 0, 
                "bossDropBonusExpireAt": {"seconds": 1795360675, "nanoseconds": 0}, 
                "wasBossDropBonusEnableAsLastDungeonEnter": false, 
                "characterThumbnail": {
                    "characterIconId": 0, 
                    "rarity": 0, 
                    "mountType": 0, 
                    "elementalType": 0
                }, 
                "emblem": {
                    "emblemId": 0, 
                    "name": "", 
                    "description": "", 
                    "rarity": 0, 
                    "imageId": 0, 
                    "text": "", 
                    "isOpenConditionPublic": false, 
                    "openCondition": ""
                }, 
                "privacySettings": 0, 
                "canTrackAd": false
            }, 
            "currentGold": {
                "userId": "1", 
                "gold": 0, 
                "paidGold": 0, 
                "freeGold": 0
            }, 
            "userWeapons": [
                {
                    "userId": "1", 
                    "userWeaponId": "1", 
                    "weaponId": 1, 
                    "isFavorite": false, 
                    "isNew": false, 
                    "status": 0, 
                    "level": 1, 
                    "exp": 0, 
                    "limitBreakStep": 0, 
                    "attack": 10, 
                    "elementalPoint": 0, 
                    "minAttack": 10, 
                    "maxAttack": 10, 
                    "minElementalPoint": 0, 
                    "maxElementalPoint": 0, 
                    "price": 0, 
                    "passiveSkillIds": [], 
                    "obtainedAt": {"seconds": 1795360675, "nanoseconds": 0}
                }
            ], 
            "userAccessories": [], 
            "userMountMonsters": [], 
            "userOptionMonsters": [], 
            "userMaterials": [], 
            "userLimitBreakMaterials": [], 
            "userUpgradeMaterials": [], 
            "userCharacters": [
                {
                    "userId": "1", 
                    "userCharacterId": "1", 
                    "playableCharacterId": 1, 
                    "level": 1, 
                    "hp": 100, 
                    "sp": 100, 
                    "attack": 10, 
                    "physicalDefense": 10, 
                    "magicalDefense": 10, 
                    "elementalPoint": 0, 
                    "playerSkillLevel": 1
                }
            ], 
            "userUtilityTickets": [], 
            "userDevilStones": [], 
            "userStamps": [], 
            "userEmblems": [], 
            "userGachaTickets": [], 
            "userFarmBuildings": [], 
            "userTradeTickets": [], 
            "generalItemDataSet": {
                "weapons": [], 
                "accessories": [], 
                "mountMonsters": [], 
                "optionMonsters": [], 
                "materials": [], 
                "limitBreakMaterials": [], 
                "upgradeMaterials": [], 
                "utilityTickets": [], 
                "playableCharacters": [], 
                "devilStones": [], 
                "stamps": [], 
                "questOnlyItems": [], 
                "emblems": [], 
                "gachaTickets": [], 
                "mountMonsterEggs": [], 
                "farmBuildings": [], 
                "itemRecipes": [], 
                "tradeTickets": [], 
                "monsters": [], 
                "characters": [], 
                "characterProfiles": [], 
                "allySkillDataSet": {"playerSkills": [], "playerTapSkills": [], "playerStepSkills": [], "optionMonsterSkills": [], "passiveSkills": []
            }, 
            "farmBuildingUpgrades": []
            }, 
            "userMountMonsterEggStatus": {
                "userId": "", 
                "eggCount": 0
            }
        }, 
        "missions": [], 
        "userFlags": [
            {
                "userId": "1", 
                "userFlagId": "1", 
                "type": 7, 
                "value": true
            }
        ], 
        "userPartyDataSet": {
            "userParties": [
                {
                    "no": 1, 
                    "userId": "1", 
                    "userPartyId": "1", 
                    "name": "Player1"
                }
            ], 
            "userPartyUnits": [
                {
                    "userId": "1", 
                    "userPartyUnitId": "1", 
                    "userPartyId": "1", 
                    "no": 1, 
                    "userCharacterId": "1", 
                    "userWeaponId": "1", 
                    "leftUserOptionMonsterId": "",
                    "rightUserOptionMonsterId": "", 
                    "userAccessory1Id": "", 
                    "userAccessory2Id": "", 
                    "uniquePlayerId": 1,
                    "playerSkillSlots": []
                }
            ], 
            "currentPartyActionDataSet": {
                "attackActions": [], 
                "additionalEffects": []
            }
        }, 
        "allySkillDataSet": {
            "playerSkills": [], 
            "playerTapSkills": [], 
            "playerStepSkills": [], 
            "optionMonsterSkills": [], 
            "passiveSkills": []
        }, 
        "userStampDeck": {
            "userId": "", 
            "deckNo": 0, 
            "slots": []
        }, 
        "userFixedMessageDeck": {
            "userId": "", 
            "deckNo": 0, 
            "slots": []
        }, 
        "userPassiveSkillTrainings": [], 
        "termsOfService": {
            "userId": "", 
            "terms": "", 
            "license": "", 
            "commerce": "", 
            "showCommerce": false, 
            "privacy": ""
        }, 
        "isJp": false
    }, 
    "bootMasterDataSet": {
        "defaultTips": [
            {
                "id": 1, 
                "title": "mocking", 
                "image": "", 
                "text": "mocking"
            }
        ], 
        "farmDataSet": {
            "farmMotionInfo": {
                "attackInfos": []
            }, 
            "farmAssignInfo": {
                "maxMountMonsterCount": 0
            }, 
            "farmBuildingInfo": {
                "maxTrainingCount": 0
            }, 
            "forceFarmUpateBaseSeconds": 0, 
            "forceFarmUpdateCosts": [], 
            "updateIntervalSeconds": 60
        }
    }, 
    "serverTime": {"seconds": 1795360675, "nanoseconds": 0}, 
    "userConstant": {
        "userId": "1", 
        "userHash": "mockhash"
    }, 
    "userSetting": {
        "userId": "1", 
        "isBirthday": true, 
        "isParentPassword": false, 
        "isStopper": false, 
        "enableCommunication": true, 
        "notificationSetting": {
            "isAllowNotification": false, 
            "isAllowEndDungeonCoolTime": false, 
            "isAllowEndSideQuestCoolTime": false
        }
    }, 
    "snsInfo": {
        "userId": "1", 
        "isRegisteredFacebookAccount": false, 
        "isRegisteredAppleAccount": false, 
        "isRegisteredSteamAccount": true
    }, 
    "generalItemDataSet": {
        "weapons": [], 
        "accessories": [], 
        "mountMonsters": [], 
        "optionMonsters": [], 
        "materials": [], 
        "limitBreakMaterials": [], 
        "upgradeMaterials": [], 
        "utilityTickets": [], 
        "playableCharacters": [], 
        "devilStones": [], 
        "stamps": [], 
        "questOnlyItems": [], 
        "emblems": [], 
        "gachaTickets": [], 
        "mountMonsterEggs": [], 
        "farmBuildings": [], 
        "itemRecipes": [], 
        "tradeTickets": [], 
        "monsters": [], 
        "characters": [], 
        "characterProfiles": [], 
        "allySkillDataSet": {
            "playerSkills": [], 
            "playerTapSkills": [], 
            "playerStepSkills": [], 
            "optionMonsterSkills": [], 
            "passiveSkills": []
        }, 
        "farmBuildingUpgrades": []
    }, 
    "clientConfigs": [], 
    "message": ""
}
```

| Field | Type | Description / Expected Values |
| :--- | :--- | :--- |
| `userDataSet` | `UserDataSetModel` |  |
| `bootMasterDataSet` | `BootMasterDataSetModel` |  |
| `serverTime` | `DateTime` |  |
| `userConstant` | `UserConstantModel` |  |
| `userSetting` | `UserSettingModel` |  |
| `snsInfo` | `UserSnsInfoModel` |  |
| `generalItemDataSet` | `GeneralItemDataSetModel` |  |
| `clientConfigs` | `ClientConfigModel[]` |  |
| `message` | `string` |  |

---

## 🧠 Reverse Engineering & Implementation Notes
* **Current Mock Behavior:** Calls ensure_registered() (likely creates/validates the account row) then returns a generic account_response("BootRegisteredInfoResponse"). No real per-account data is populated yet.
See [boot.py][../../../serverfiles/routes/boot.py#8] for current implementation
* **Client Dependencies / Edge Cases:** If this call fails or returns a non-zero status, the client likely halts the boot flow and shows a registration/login error. Missing the "BootRegisteredInfoResponse" key will probably cause a KeyNotFoundException on the client side.
* **Database Requirements:** Needs a users / accounts table with at minimum user_id, created_at, and registered (bool) to back the ensure_registered() call.