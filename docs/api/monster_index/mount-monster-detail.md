# Endpoint: `POST /api/monster-index/mount-monster-detail`

* **Status:** 🟡 Mock / Skeleton
* **Category:** Monsters (Monster Index, Mount Monster Detail)
* **Related Game Classes (Cpp2IL):** `Ammo.MonsterIndexMountMonsterDetailApi`, `Ammo.MonsterIndexMountMonsterDetailRequest`, `Ammo.MonsterIndexMountMonsterDetailResponse`, `Ammo.MountMonsterModel`, `Ammo.MonsterModel`, `Ammo.MonsterDictionaryMountMonsterDetailScene`, `Ammo.MonsterDictionaryMonsterDetailSceneBase<,>`, `Ammo.MonsterDictionarySceneController`, `Ammo.MountMonsterBuildParam`, `Ammo.CharacterBuilder` (`SimpleMountMonster`)

---

## 📋 Overview
Called when an entry of the mount monster list is opened. The response contains the master data, descriptions, strong and weak stats, default skills, parent monsters for breeding and drop quests. The client builds the detail view, including the 3D model, from it (`MonsterDictionarySceneController.Setup(MountMonsterModel, isSilhouette)`).

The HTTP method: the API constructor sets a method field of `2`, which I read as POST based on the pattern across all 220 `*Api` classes. The constructor also sets a flag byte of `1`; its meaning is unknown.

---

## 📥 Request (Client ➔ Server)

### Headers (if special)
```http
Accept: application/msgpack
Accept-Encoding: gzip
Authorization: Bearer <auth_token>
```

### Payload Structure
```json
{ "mountMonsterId": 1000001 }
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `mountMonsterId` | `long` | Yes | `mountMonsterId` from the list response |

---

## 📤 Response (Server ➔ Client)

### Response Headers
```http
Content-Type: application/msgpack
```

### Expected Structure (MessagePack map, shown as JSON)
```json
{
  "commonResource": { "subNotifications": [], "badges": [] },
  "mountMonster": {
    "mountMonsterId": 1000001, "name": "Test", "indexNo": 1, "monsterId": 1000001,
    "iconId": 1000001, "rarity": 1, "mountType": 1, "isDefault": false, "grade": 1,
    "sequenceId": 1000001, "longTapSkillId": 0,
    "baseHp": 0, "baseSp": 0, "baseAttack": 0, "basePhysicalDefense": 0, "baseMagicalDefense": 0,
    "elementalType": 1, "baseElementalPoint": 0,
    "hpLevelCoefficient": 1.0, "spLevelCoefficient": 1.0, "attackLevelCoefficient": 1.0,
    "physicalDefenseLevelCoefficient": 1.0, "magicalDefenseLevelCoefficient": 1.0,
    "elementalPointLevelCoefficient": 1.0,
    "hpExpCoefficient": 1.0, "spExpCoefficient": 1.0, "attackExpCoefficient": 1.0,
    "physicalDefenseExpCoefficient": 1.0, "magicalDefenseExpCoefficient": 1.0,
    "elementalPointExpCoefficient": 1.0,
    "minTrainedHpLimit": 0, "maxTrainedHpLimit": 0,
    "minTrainedSpLimit": 0, "maxTrainedSpLimit": 0,
    "minTrainedAttackLimit": 0, "maxTrainedAttackLimit": 0,
    "minTrainedPhysicalDefenseLimit": 0, "maxTrainedPhysicalDefenseLimit": 0,
    "minTrainedMagicalDefenseLimit": 0, "maxTrainedMagicalDefenseLimit": 0,
    "minTrainedElementalPointLimit": 0, "maxTrainedElementalPointLimit": 0,
    "price": 0, "hateId": 0, "playerSkill1Id": 0
  },
  "monster": {
    "monsterId": 1000001, "name": "Test", "evolutionStep": 1, "blowRate": 0,
    "category": 0, "species": 1, "voiceCategory": 0,
    "modelId": 1000001, "motionId": 1000001, "sequenceId": 1000001
  },
  "dropQuests": [],
  "descriptions": [ { "text": "Test", "iconType": 1, "isLocked": false } ],
  "strongStatusTypes": [2],
  "weakStatusTypes": [3],
  "defaultPlayerSkills": [],
  "rareDefaultPlayerSkills": [],
  "defaultPassiveSkills": [],
  "parentMountMonsterThumbnails1": [],
  "parentMountMonsterThumbnails2": [],
  "hasOtherBreedingRecipe": false
}
```

| Field | Type | Description / Expected Values |
| :--- | :--- | :--- |
| `mountMonster` | object | `MountMonsterModel`, fields below |
| `monster` | object | `MonsterModel`, fields below. `monsterId` should match `mountMonster.monsterId` |
| `dropQuests` | array | `ModifiedQuestModel[]` (`name`, `type`, `quest`). Deeply nested; `[]` is enough for a mock |
| `descriptions` | array | `MonsterDescriptionModel[]`: `text` (string), `iconType` (int: 1–8 or 100 = `ReserveTempLocked`), `isLocked` (bool) |
| `strongStatusTypes` | array | `MonsterTrainedStatusType[]` as int: 0 None, 1 Random, 2 HP, 3 Attack, 4 PhysicalDefense, 6 MagicalDefense, 7 Element, 8 SP (5 does not exist) |
| `weakStatusTypes` | array | same as `strongStatusTypes` |
| `defaultPlayerSkills` | array | `PlayerSkillModel[]`, very large; `[]` is enough for a mock |
| `rareDefaultPlayerSkills` | array | `PlayerSkillModel[]`; `[]` is enough for a mock |
| `defaultPassiveSkills` | array | `PassiveSkillModel[]`; `[]` is enough for a mock |
| `parentMountMonsterThumbnails1` | array | `MountMonsterThumbnailModel[]`, same structure as in the list endpoint (`mount-monster`): `indexNo` (int), `mountMonsterId` (long), `rarity`, `elementalType`, `mountType`, `grade` (int), `monsterThumbnail` (object with `monsterId`, `name`, `iconId`, `monsterIndexStatus`, `monsterModelId`) |
| `parentMountMonsterThumbnails2` | array | `MountMonsterThumbnailModel[]` |
| `hasOtherBreedingRecipe` | `bool` | Whether further breeding recipes exist |

**`MountMonsterModel`**

| Field | Type | Description |
| :--- | :--- | :--- |
| `mountMonsterId` | `long` | ID |
| `name` | `string` | Display name |
| `indexNo` | `int` | Index number |
| `monsterId` | `int` | Reference to `monster.monsterId` |
| `iconId` | `int` | Icon asset `ui/monster/icon/m_{id:D7}` |
| `rarity` | `int` | 0–8 |
| `mountType` | `int` | 0–5 |
| `isDefault` | `bool` | Unknown purpose |
| `grade` | `int` | Grade |
| `sequenceId` | `int` | In initial tests this was equal to the iconId and modelId |
| `longTapSkillId` | `int` | Associated Skill ID |
| `baseHp`, `baseSp`, `baseAttack`, `basePhysicalDefense`, `baseMagicalDefense`, `baseElementalPoint` | `int` | Base values |
| `elementalType` | `int` | 0–6 |
| `hpLevelCoefficient`, `spLevelCoefficient`, `attackLevelCoefficient`, `physicalDefenseLevelCoefficient`, `magicalDefenseLevelCoefficient`, `elementalPointLevelCoefficient` | `float` | Level coefficients |
| `hpExpCoefficient`, `spExpCoefficient`, `attackExpCoefficient`, `physicalDefenseExpCoefficient`, `magicalDefenseExpCoefficient`, `elementalPointExpCoefficient` | `float` | Experience coefficients |
| `minTrainedHpLimit`, `minTrainedSpLimit`, `minTrainedAttackLimit`, `minTrainedPhysicalDefenseLimit`, `minTrainedMagicalDefenseLimit`, `minTrainedElementalPointLimit` | `int` | Lower limits for training |
| `maxTrainedHpLimit`, `maxTrainedSpLimit`, `maxTrainedAttackLimit`, `maxTrainedPhysicalDefenseLimit`, `maxTrainedMagicalDefenseLimit`, `maxTrainedElementalPointLimit` | `int` | Upper limits for training |
| `price`, `hateId`, `playerSkill1Id` | `int` | ❓ |

**`MonsterModel`**

| Field | Type | Description |
| :--- | :--- | :--- |
| `monsterId` | `int` | Monster ID |
| `name` | `string` | Display name |
| `evolutionStep` | `int` | Evolution step |
| `blowRate` | `int` | ❓ |
| `category` | `int` | 0 Normal, 1 Rare |
| `species` | `int` | 0 None, 1 Punin, 2 Goblin, 3 Huwamimi, 4 Volk, 5 Mushru, 6 Golem, 7 Pix, 8 Ele, 9 Mananium, 10 Chate, 11 Flolo, 12 Guruda, 13 TheFanatic, 14 Wyrm, 15 Bugreus, 16 Taimai, 17 Gnome, 18 Zeele, 19 Kicklle |
| `voiceCategory` | `int` | `MonsterVoiceCategory` 0–25 (0 None, 1 SmallDragon, 2 Dragon, 3 BigDragon, 4 Cute, 5 Carrac, 6 Bird, 7 Bird2, 8 EvilInsect, 9 Insect, 10 Beast, 11 EvilBeast, 12 Frog, 13 Machine, 14 Golem, 15 Lion, 16 Flower1, 17 Flower2, 18 Sheep, 19 Sea, 20 Fox, 21 Mystery1, 22 Mystery2, 23 Mystery3, 24 Dog, 25 Rat) |
| `modelId` | `int` | Model bundle `character/monster/model/m_{id:D7}` |
| `motionId` | `int` | Animation bundle (see notes) |
| `sequenceId` | `int` | Sequence bundle (see notes) |

---

## 🧠 Reverse Engineering & Implementation Notes
* **Current Mock Behavior:** All fields filled, lists with complex types left empty. The detail view loads. In the test, `mountMonster.iconId`, `monster.modelId`, `motionId` and `sequenceId` were all set to `1000001`.
* **Client Dependencies / Edge Cases:**
  * The view loads model, motion and sequence bundles. If one is missing, `Player.log` shows `Unable to open archive file …/StreamingAssets/1/w/<a>/<b>/<name>` and the game reports "Failed to load".
  * Send float fields as real floats and avoid `0` for the coefficients (in case the UI divides by them when it calculates stats).
  * For how asset names are resolved, and why missing bundles show up as numeric paths, see `option-monster-detail`.
  * HTTP `404` shows a connection-error dialog and the game keeps running; HTTP `200` with an empty or invalid body freezes the game without a crash.
  * Invalid or non resolveable asset Ids force a "failed to load asset" error and failback to the main menu.
* **Database Requirements:** Master data per mount monster (stats, skills, parents) and drop quests per monster. 