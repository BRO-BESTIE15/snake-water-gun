# 🐍 Snake Water Gun Game
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-blue)
![Beginner](https://img.shields.io/badge/Level-Beginner-orange)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)

A simple **Snake 🐍, Water 💧, Gun 🔫** game made in Python.

📄 **Source Code:** `src/cli.py` and `src/engine.py`

> `archive/snake_water_gun_cli.py` is a legacy single-file prototype kept for reference. The active project uses the modular `cli.py` + `engine.py` structure.

Play **Snake, Water, Gun** against the computer! Before the game starts, you can choose how many rounds you want to play. The computer randomly selects its moves, and the winner of each round is determined by the game rules. The project tracks score across rounds and shows the final winner at the end.

## ✨ Current Features (MVP)

- 🎲 Random computer moves using Python's `random.choice()`
- 🎮 User-configurable number of rounds
- ✅ Robust input validation with clear error messages
- 📊 Live score tracking (player, computer, draws)
- 🧾 Final statistics: round win percentage and final winner announcement
- 🧠 Lookup table-based game logic (fast, easy to reason about)
- 🎨 ANSI-coloured terminal output for clearer win/lose/draw messages
- 🔁 "Play again" prompt to repeat games without restarting the program
- 🧩 Modular structure with separate `cli.py` and `engine.py` modules (easy to read and extend)

## 🚀 How to Run

From a fresh clone, run:

```bash
python src/cli.py
```

Requires Python 3.x. No external dependencies are required to play the game. A terminal that supports ANSI escape codes is recommended for the coloured output.

### Optional packaged build

This repository also contains a PyInstaller spec file at `src/snake-water-gun.spec` for creating a standalone executable. This is optional and not required for normal gameplay.

```bash
python -m PyInstaller src/snake-water-gun.spec
```

## 🎮 Controls

| Input | Move |
|------:|------|
| `0` | 🐍 Snake |
| `1` | 💧 Water |
| `2` | 🔫 Gun |

First, enter the number of rounds you want to play. Then, enter the number corresponding to your move when prompted.

## 📷 Example run

```
|| 🐍 SNAKE WATER GUN 🔫 ||

How many rounds would you like to play? 5

══════════ ROUND 1 ══════════
        Choose your move:
        0 → 🐍 Snake
        1 → 💧 Water
        2 → 🔫 Gun
Your choice: 1
══════════════════════════════════
Your move is Water
Computer move is Water
It's a draw

Score → You: 0 | Computer: 0 | Draws: 1
══════════════════════════════════

══════════ ROUND 2 ══════════
        Choose your move:
        0 → 🐍 Snake
        1 → 💧 Water
        2 → 🔫 Gun
Your choice: 0
══════════════════════════════════
Your move is Snake
Computer move is Snake
It's a draw

Score → You: 0 | Computer: 0 | Draws: 2
══════════════════════════════════

══════════ ROUND 3 ══════════
        Choose your move:
        0 → 🐍 Snake
        1 → 💧 Water
        2 → 🔫 Gun
Your choice: 2
══════════════════════════════════
Your move is Gun
Computer move is Snake
You win

Score → You: 1 | Computer: 0 | Draws: 2
══════════════════════════════════

══════════ ROUND 4 ══════════
        Choose your move:
        0 → 🐍 Snake
        1 → 💧 Water
        2 → 🔫 Gun
Your choice: 1
══════════════════════════════════
Your move is Water
Computer move is Water
It's a draw

Score → You: 1 | Computer: 0 | Draws: 3
══════════════════════════════════

══════════ ROUND 5 ══════════
        Choose your move:
        0 → 🐍 Snake
        1 → 💧 Water
        2 → 🔫 Gun
Your choice: 0
══════════════════════════════════
Your move is Snake
Computer move is Water
You win

Score → You: 2 | Computer: 0 | Draws: 3
══════════════════════════════════
Round win % : 40.00
Player: 2
Computer: 0
Draws: 3
══════════════════════════════════
FINAL RESULT:
YOU WIN
Another game? (y/n) N

Thanks for playing! 👋

[Program finished]
```

## 📚 Concepts Used

- Functions
- Lists and 2D lists (lookup table)
- Dictionaries
- `random.choice()`
- Loops and control flow
- Input validation (`try`/`except`)
- Terminal colouring via ANSI escape codes
- Modular code organization

## 📜 Rules

- Snake 🐍 drinks Water 💧
- Water 💧 douses Gun 🔫
- Gun 🔫 kills Snake 🐍
- Same moves result in a Draw 🤝

## 📁 Project Structure

```
./
├── src/
│   ├── cli.py        # User interface and game loop
│   ├── engine.py     # Game logic and result calculations
│   └── snake-water-gun.spec  # Optional PyInstaller packaging config
└── archive/
    └── snake_water_gun_cli.py  # Legacy single-file prototype retained for reference
```

## 🗺️ Roadmap

The project has already completed the modular refactor and the core gameplay feature work that was previously tracked as issues. The currently active roadmap items are the enhancements still planned below:

| Issue | Feature | Status |
|-------|---------|--------|
| [#1](https://github.com/BRO-BESTIE15/snake-water-gun/issues/1) | Colored terminal output | Completed |
| [#2](https://github.com/BRO-BESTIE15/snake-water-gun/issues/2) | Play again prompt | Completed |
| [#3](https://github.com/BRO-BESTIE15/snake-water-gun/issues/3) | Win percentage statistics | Completed |
| [#10](https://github.com/BRO-BESTIE15/snake-water-gun/issues/10) | Separate game engine and CLI into modular files | Completed |
| [#4](https://github.com/BRO-BESTIE15/snake-water-gun/issues/4) | Persistent game statistics using JSON | Open |
| [#5](https://github.com/BRO-BESTIE15/snake-water-gun/issues/5) | Main menu and match history | Open |
| [#6](https://github.com/BRO-BESTIE15/snake-water-gun/issues/6) | Game settings (preferences file) | Open |
| [#7](https://github.com/BRO-BESTIE15/snake-water-gun/issues/7) | Pygame graphical version | Open |
| [#8](https://github.com/BRO-BESTIE15/snake-water-gun/issues/8) | Add timed delays for improved UX | Open |

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

Made as a beginner Python practice project. 🚀
