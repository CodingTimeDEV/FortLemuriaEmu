# Endpoint: `GET /api/monster-index/top`

* **Status:** 🟡 Mock / Skeleton
* **Category:** Monsters (Monster Index / Dictionary)
* **Related Game Classes (Cpp2IL):** `Ammo.MonsterIndexTopApi`, `Ammo.MonsterIndexTopRequest`, `Ammo.MonsterIndexTopResponse`, `Ammo.MonsterDictionaryTopScene` (`<OnCreateSceneImpl>d__5`), `Ammo.MonsterDictionaryTopViewModel`, `Ammo.CommonResourceModel`, `Ammo.BadgeModel`, `Ammo.NetworkManager`

---

## 📋 Overview
Called when the player opens the start page of the monster index. The response has no fields of its own, only the inherited `commonResource` block with badges. Afterwards the scene reads two badges from the local database (`BadgeModel` with `Type == 18` and `Type == 19`), builds `MonsterDictionaryTopViewModel.Setup(mountMonster, optionMonster)` from them and loads the UI `New/Dictionary/UIDictionarySelectMenu`. The two badges most likely belong to the "Mount Monster" and "Option Monster" button.

---

## 📥 Request (Client ➔ Server)

### Headers (if special)
```http
Accept: application/msgpack
Accept-Encoding: gzip
Authorization: Bearer <auth_token>
```

### Payload Structure
No body. `MonsterIndexTopRequest` has no fields.

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| – | – | – | – |

---

## 📤 Response (Server ➔ Client)

### Response Headers
```http
Content-Type: application/msgpack
x-server-time: 1795745291
AssetBundle-Manifest: local_latest
```
`x-server-time` is optional.

### Expected Structure (MessagePack map, shown as JSON)
```json
{
  "commonResource": {
    "subNotifications": [],
    "badges": [
      { "type": 18, "enable": false, "count": 0 },
      { "type": 19, "enable": false, "count": 0 }
    ]
  }
}
```

| Field | Type | Description / Expected Values |
| :--- | :--- | :--- |
| `commonResource` | object | `CommonResourceModel` |
| `commonResource.subNotifications` | array | `SubNotificationModel[]`. `[]` is enough. Fields: `text` (string), `type` (int, `SubNotificationType`, values), `noticeAt` (DateTime, MessagePack encoding), `param` (string) |
| `commonResource.badges` | array | `BadgeModel[]`. The scene looks up `type` 18 and 19 in it (required, see notes) |
| `commonResource.badges[].type` | `int` | `BadgeType`. 18 and 19 are read. Meaning probably mount / option monster button |
| `commonResource.badges[].enable` | `bool` | Probably an "exclamation mark" badge (`BadgeModel.IsExclamation()`), maybe to show new available entries |
| `commonResource.badges[].count` | `int` | Probably a number badge (`BadgeModel.IsNumber()`) |

---

## 🧠 Reverse Engineering & Implementation Notes
* **Current Mock Behavior:** Returns the map above, i.e. both badges with `enable: false, count: 0`. The client then loads the dictionary menu.
* **Client Dependencies / Edge Cases:**
  * With `badges: []` the game froze (observed; `Player.log` showed `Curl error 42: Callback aborted`). It only worked once both badges (18 and 19) were present. The cause is probably a `null` access while building the view model (not proven).
  * An empty body, or JSON instead of MessagePack, did not work.
  * HTTP `404` shows a connection-error dialog and the game keeps running; HTTP `200` with an empty body freezes the game without a crash.
* **Database Requirements:** Per player, the "new" state of the dictionary entries (drives `enable` / `count` of the two badges). This is a recommendation and cannot be read from the client.