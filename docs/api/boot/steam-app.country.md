# Endpoint: `/api/boot/steam-app-country`

* **Status:** 🟡 Mock / Skeleton
* **Category:** Auth / Game Setup
* **Related Game Classes (Cpp2IL):** Req: BootSteamAppCountryRequest ; Resp: BootSteamAppCountryResponse

---

## 📋 Overview
Called during boot to determine the player's region/country code, presumably derived from the Steam store region or IP geolocation. 
The client uses this value to select the correct content pool, locale strings, or regional restrictions before proceeding with the full asset download.

Identified by steam ticket id.

---

## 📥 Request (Client ➔ Server)

### Headers (if special)
```http
Unknown
```

### Payload Structure
```json
{
  "ticket": 12345
}
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ticket` | `string` | Yes | Steam Session Ticket |

---

## 📤 Response (Server ➔ Client)

### Expected JSON Structure
```json
{
  "country": 2
}
```

| Field | Type | Description / Expected Values |
| :--- | :--- | :--- |
| `country` | `int` | `0` = Global; `2` = English |

---

## 🧠 Reverse Engineering & Implementation Notes
* **Current Mock Behavior:** Always returns `{"country": 1}` regardless of the caller. No DB lookup, no steam ticket to locale lookup.
* **Client Dependencies / Edge Cases:** The client probably switches locale strings, available DLC, or shop content based on this int. Returning an unrecognised value may cause a default fallback or a crash. The full enum mapping should be extracted from the client's `AppCountry` enum.
* **Database Requirements:** For now it's sufficient to respond with a static value (change to `2`=English), for actual implementation a steam ticket lookup or other validation needs to be implemented.
