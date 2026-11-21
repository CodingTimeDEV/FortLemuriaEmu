# Contributing to FortLemuriaEmu

First off, thank you for considering contributing to **FortLemuriaEmu**! 

You **do not** need to be a senior developer or a reverse engineering expert to help us bring *Volzerk: Monsters and Lands Unknown* back. In fact, most of our reverse engineering and server development is done using **AI Agents**. If you know how to chat with an AI and follow step-by-step instructions, you can make a huge impact!

---

## 🧠 How We Work (AI-Assisted Reverse Engineering)

Instead of manually reading thousands of lines of raw code, we let AI agents do the heavy lifting. By connecting specialized analysis tools to an AI assistant, the AI can inspect the game's files, understand what the game expects from the server, and help write the Python code for `/serverFiles`.

* **AI Assistants:** This project was bootstrapped using **GitHub Copilot**, but other AI coding agents (such as **Claude Code**, **Cursor**, **Codex**, or **Gemini CLI**) work just as well—or even better!
* **Agent Tools (REA):** We connect **[REA (Reverse Engineer Anything)](https://github.com)** to our AI agent. This gives the AI "hands and eyes" to inspect binaries, analyze IL2CPP metadata, and trace game logic automatically.

---

## 🛠️ Step-by-Step Setup Guide

If you want to investigate unknown API endpoints or implement missing server features with your AI, follow these simple steps:

### Step 1: Extract the Game Files (Cpp2IL)
Because *Volzerk* is built with Unity (IL2CPP), its code needs to be unpacked into a readable format before the AI can easily analyze it. We use **[Cpp2IL](https://github.com)** for this.

1. Download the latest release of **Cpp2IL** from their GitHub repository.
2. Open your terminal / command prompt and run Cpp2IL on your local copy of the game twice—once to get readable C# structure (`diffable-cs`) and once to get detailed instruction logic (`isil`):

   ```bash
   # 1. Extract readable C# class/method structures
   Cpp2IL --game-path="C:\(\Path\To\Your\Game\)" --output-as diffable-cs --output-to ./extracted_cs

   # 2. Extract detailed ISIL instructions for deeper logic analysis
   Cpp2IL --game-path="C:\(\Path\To\Your\Game\)" --output-as isil --output-to ./extracted_isil
   ```
   *(Note: Never upload the extracted game files or copyrighted assets to this GitHub repository! Keep them strictly local on your PC.)*

### Step 2: Connect REA to Your AI Agent
To let your AI agent use professional reverse engineering tools automatically:

1. Make sure you have **Node.js** installed on your computer.
2. Open your terminal and run the official REA setup wizard:
   ```bash
   npx rea-agents setup
   ```
3. Follow the on-screen menu to select your preferred AI agent (e.g., Copilot, Cursor, Claude Code) and approve the changes.
4. Restart your AI editor/agent so it loads the new REA tools.

### Step 3: Ask the AI to Investigate!
Now you are ready to explore! Open your local `FortLemuriaEmu` folder alongside your extracted game files in your AI editor and ask natural-language questions, such as:

> *"Using REA, inspect the extracted C# and ISIL files in `./extracted_cs` and `./extracted_isil` to find out what JSON payload the game expects when loading the Home Farm NPCs or calling `/api/example`. Document the findings following `docs/_TEMPLATE_ENDPOINT.md` and implement the endpoint in `/serverFiles`."*

---

## 📌 Ways You Can Help (Even Without Coding!)

* **Documenting Endpoints (`/docs`):** Ask your AI to find API routes, request parameters, and response structures in the extracted files, then submit the Markdown summaries to `/docs` using `docs/_TEMPLATE_ENDPOINT.md`.
* **Implementing Server Logic (`/serverFiles`):** Have your AI translate game logic into clean Python endpoints for our server emulator.
* **Testing & Bug Reporting:** Run the local server, try out the game using `/patchScripts`, and open an **Issue** if something crashes or behaves unexpectedly.
* **Screenshots (`/progressImg`):** Share screenshots of newly working menus, battles, or features!

---

## 📤 How to Submit Your Changes

1. **Fork** this repository (click the "Fork" button at the top right of the GitHub page).
2. **Clone** your fork to your computer and create a new branch for your work:
   ```bash
   git checkout -b feature/my-new-endpoint
   ```
3. **Add your changes** to `/docs`, `/serverFiles`, or `/patchScripts`.
   * ⚠️ **Important:** Double-check that you are **not** uploading any copyrighted game binaries, APKs, or full Cpp2IL dumps! Only upload our own documentation, scripts, and Python server code.
4. **Commit and Push** your changes to your fork, then open a **Pull Request** on the main `FortLemuriaEmu` repository.
5. Briefly describe what you discovered or added (mentioning which AI/tools you used is always helpful!).

Thank you for helping keep *Volzerk* alive! 🐉✨
