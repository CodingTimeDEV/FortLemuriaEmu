# Endpoint: `POST /api/monster-index/option-monster`

* **Status:** 🟡 Mock / Skeleton
* **Category:** Monsters (Monster Index, Option Monsters)
* **Related Game Classes (Cpp2IL):** `Ammo.MonsterIndexOptionMonsterApi`, `Ammo.MonsterIndexOptionMonsterRequest`, `Ammo.MonsterIndexOptionMonsterResponse`, `Ammo.OptionMonsterThumbnailModel`, `Ammo.MonsterThumbnailModel`, `Ammo.MonsterDictionaryTopScene` (`<OpenOptionMonsterList>d__11`), `Ammo.MonsterDictionaryOptionMonsterListScene`, `Ammo.MonsterDictionaryMonsterSelectViewModel`

---

## 📋 Overview
Called when the player opens the "Option Monster" section of the monster index. Structure and behavior match the mount monster list, only the entries have different fields (role instead of rarity, mount type and grade).

The HTTP method: the API constructor sets a method field of `2`, which I read as POST based on the pattern across all 220 `*Api` classes. The constructor also sets two flag bytes (`257`); their meaning is unknown.

---

## 📥 Request (Client ➔ Server)

### Headers (if special)
```http
Accept: application/msgpack
Accept-Encoding: gzip
Authorization: Bearer <auth_token>
```

### Payload Structure
No body. `MonsterIndexOptionMonsterRequest` has no fields.

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| – | – | – | – |

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
  "thumbnails": [
    {
      "indexNo": 1,
      "optionMonsterId": 101001610,
      "elementalType": 1,
      "optionMonsterRole": 1,
      "monsterThumbnail": {
        "monsterId": 101001610,
        "name": "Test",
        "iconId": 101001610,
        "monsterIndexStatus": 4,
        "monsterModelId": 101001610
      }
    }
  ]
}
```

| Field | Type | Description / Expected Values |
| :--- | :--- | :--- |
| `thumbnails` | array | `OptionMonsterThumbnailModel[]` |
| `thumbnails[].indexNo` | `int` | Index number |
| `thumbnails[].optionMonsterId` | `long` | ID used for `option-monster-detail` |
| `thumbnails[].elementalType` | `int` | 0 None, 1 Fire, 2 Wind, 3 Thunder, 4 Water, 5 Light, 6 Dark |
| `thumbnails[].optionMonsterRole` | `int` | 1 Attacker, 2 Tanker, 3 Healer, 4 Buffer, 5 Debuffer (starts at **1**; `0` is not a defined value) |
| `thumbnails[].monsterThumbnail` | object | `MonsterThumbnailModel`, identical to the mount monster list: `monsterId` (int), `name` (string), `iconId` (int), `monsterIndexStatus` (int: 0 Unidentified, 1 NewIdentified, 2 Identified, 3 NewObtained, 4 Obtained), `monsterModelId` (int) |

There is no `rarity`, `mountType` or `grade`. Note that the field is called `optionMonsterRole` here but `role` in the detail response.

---

## 🧠 Reverse Engineering & Implementation Notes
* **Current Mock Behavior:** Returns one entry with `iconId: 101001610`. No error was reported.
* **Client Dependencies / Edge Cases:**
  * As with mount monsters, the icon bundle `ui/monster/icon/m_{iconId:D7}` must exist locally. `ui/monster/icon/m_101001610` is listed in the asset manifest.
  * `UpdateDatabase()` on the response and on each entry writes into the client database.
  * HTTP `404` shows a connection-error dialog and the game keeps running; HTTP `200` with an empty or invalid body freezes the game without a crash.
* **Database Requirements:** A master table of option monsters and, per player, the index status.