# FortLemuriaEmu

**FortLemuriaEmu** is an open-source server emulator preservation project aimed at bringing *Volzerk: Monsters and Lands Unknown* back to life. 

Our goal is to provide a free, public community server for everyone to play, while also offering the complete server software for anyone who wishes to host their own private instance.

> **Disclaimer:** FortLemuriaEmu is a non-profit, fan-made preservation project. We are not affiliated with, endorsed, or sponsored by COLOPL, Inc. or any of its subsidiaries. All game assets and trademarks belong to their respective owners.

---

## 📊 Project Status & Roadmap

**Current State:** Early Prototype (Mock Server) — The game boots and reaches the Lobby / Home Farm, though the area is currently empty and most endpoints still return placeholder responses.

### ✅ Working
* **Client Boot & Lobby Entry:** The game client successfully connects to the local server, bypasses initial checks, and loads into the Lobby / Home Farm area.

### 🚧 Work in Progress (WIP)
* **Prologue Sequence:** Currently skipped by default via `MOCK_SKIP_PROLOGUE` in `serverFiles/config.py`. Active work is underway to properly handle the prologue flow and progression flags.
* **Lobby & Home Farm Population:** Investigating the required payload data to spawn NPCs, monsters, and interactive objects in the hub area.

### 📋 Planned / TODO
* **Database Transition & Persistence:** Move away from the current `.txt` file user storage (which does not yet load 100% of player data reliably) to a proper database (e.g., SQLite).
* **Real User & Session Handling:** Replace mock login flows with proper multi-user authentication, session management, and connection handling.
* **Full API Implementation:** Replace skeleton/incomplete JSON mock responses with dynamic, state-driven server logic across all gameplay endpoints.

---

## 🌟 Features & Goals
* **Public Community Server:** Play online with others once the core server functionality and database persistence are stable (Server details & status: *Coming Soon*).
* **Self-Hosting Ready:** Lightweight Python-based server architecture allowing you to run your own local or private server.
* **Open Documentation:** Full transparency on network protocols, packet structures, and API endpoints discovered during reverse engineering.

---

## 📂 Repository Structure

```text
FortLemuriaEmu/
├── docs/           # Research notes, analysis summaries, and extracted API endpoint lists
├── patchScripts/   # Python scripts to patch game client files (see internal README for usage)
├── progressImg/    # Screenshots and visual previews of the current emulator state
└── serverFiles/    # Core server emulator source code written in Python (including config.py)
```

* **`/docs`**: Contains technical documentation in Markdown format, including protocol analysis summaries and known API routes.
* **`/patchScripts`**: Houses the Python utilities required to redirect the game client to custom server endpoints. Check [`patchScripts/README.md`](patchScripts/README.md) for detailed instructions.
* **`/progressImg`**: A gallery showcasing current milestones, in-game tests, and working features.
* **`/serverFiles`**: The backend logic, mock JSON handlers, and `config.py` powering the emulated server.

---

## 🚀 Getting Started

*(Note: The project is currently in an early mock-server stage. Setup instructions will be expanded as core systems are completed.)*

### Prerequisites
* Python 3.10 or higher
* A clean copy of the game client

### Quick Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/CodingTimeDEV/FortLemuriaEmu
   cd FortLemuriaEmu
   ```
2. **Patch the client:**
   Navigate to the `/patchScripts` directory and follow the instructions in its local README to point your client to your target server.
3. **Configure & Run the server:**
   Navigate to `/serverFiles`, check `config.py` (e.g., `MOCK_SKIP_PROLOGUE`), and start the main server script.

---

## 🤝 Contributing

Contributions from developers, reverse engineers, and testers are always welcome! Most of our reverse engineering is done using **AI Agents**, so you don't need to be a senior developer to help out.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For a beginner-friendly guide on using AI agents (like GitHub Copilot + REA) and Cpp2IL to help us, please read our [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📜 License

This project is licensed under the GNU AGPLv3 License - see the [LICENSE](LICENSE) file for details.
