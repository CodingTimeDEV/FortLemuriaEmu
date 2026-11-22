# Endpoint: `/api/boot/app-age`

* **Status:** 🟡 Mock / Skeleton
* **Category:** Boot / Auth
* **Related Game Classes (Cpp2IL):** Req: BootAppAgeRequest; Resp: BootAppAgeResponse

---

## 📋 Overview
Called during boot to fetch the player's age-verification tier. The value is used by the client to gate age-restricted content (e.g., certain cosmetics, text filters, or parental-lock features). 

The games implementation is an enum rather than a literal age.

---

## 📥 Request (Client ➔ Server)

### Headers (if special)
```http
"Host": "127.0.0.1:8092",
"User-Agent": "curl/8.13.0", 
"Accept": "*/*"
```

### Payload Structure
```json
null
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |

---

## 📤 Response (Server ➔ Client)

### Expected JSON Structure
```json
{
  "appAge": 2
}
```

| Field | Type | Description / Expected Values |
| :--- | :--- | :--- |
| `appAge` | `EAppAge/int` | Age flags in range of `0-2`. `0` = UnderThirteen, `1` = UnderSixteen, `2` SixteenOrOver |

---

## 🧠 Reverse Engineering & Implementation Notes
* **Current Mock Behavior:** Currently hardcoded to `2`, no actual per user lookup; For the sake of this project this might be sufficient in the long term.
* **Client Dependencies / Edge Cases:** Unkown
* **Database Requirements:** For actual implementation it should be queried from a `user_age` table
