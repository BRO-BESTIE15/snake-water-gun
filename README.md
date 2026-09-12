# 🐍 Snake Water Gun Game
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Beginner](https://img.shields.io/badge/Level-Beginner-orange)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)

A simple **Snake 🐍, Water 💧, Gun 🔫** game made in Python.

📄 **Source Code:** `src/snake_water_gun_cli.py`

Play **Snake, Water, Gun** against the computer! Before the game starts, you can choose how many rounds you want to play. The computer randomly selects its moves, and the winner of each round is determined by a lookup table.

## ✨ Features

- 🎲 Random computer moves using Python's `random.choice()`
- 🎮 User-configurable number of rounds
- ✅ Robust input validation with clear error messages
- 📊 Live score tracking (player, computer, draws)
- 🧾 Final statistics: win percentage and final winner announcement
- 🧠 Lookup table-based game logic (fast, easy to reason about)
- 🎨 ANSI-coloured terminal output for clearer win/lose/draw messages
- 🔁 "Play again" prompt to repeat games without restarting the program
- 🧩 Small, single-file CLI (easy to read and extend)

## 🚀 How to Run

From a fresh clone, run:

```bash
python src/snake_water_gun_cli.py
```

Requires Python 3.x. No external dependencies. A terminal that supports ANSI escape codes is recommended for the coloured output.

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
═══════════════════════════════════
Your move is Water
Computer move is Water
It's a draw

Score → You: 0 | Computer: 0 | Draws: 1
═══════════════════════════════════

══════════ ROUND 2 ══════════
        Choose your move:
        0 → 🐍 Snake
        1 → 💧 Water
        2 → 🔫 Gun
Your choice: 0
═══════════════════════════════════
Your move is Snake
Computer move is Snake
It's a draw

Score → You: 0 | Computer: 0 | Draws: 2
═══════════════════════════════════

══════════ ROUND 3 ══════════
        Choose your move:
        0 → 🐍 Snake
        1 → 💧 Water
        2 → 🔫 Gun
Your choice: 2
═══════════════════════════════════
Your move is Gun
Computer move is Snake
You win

Score → You: 1 | Computer: 0 | Draws: 2
═══════════════════════════════════

══════════ ROUND 4 ══════════
        Choose your move:
        0 → 🐍 Snake
        1 → 💧 Water
        2 → 🔫 Gun
Your choice: 1
═══════════════════════════════════
Your move is Water
Computer move is Water
It's a draw

Score → You: 1 | Computer: 0 | Draws: 3
═══════════════════════════════════

══════════ ROUND 5 ══════════
        Choose your move:
        0 → 🐍 Snake
        1 → 💧 Water
        2 → 🔫 Gun
Your choice: 0
═══════════════════════════════════
Your move is Snake
Computer move is Water
You win

Score → You: 2 | Computer: 0 | Draws: 3
═══════════════════════════════════
Win % : 40.00
Player: 2
Computer: 0
Draws: 3
═══════════════════════════════════
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

## 📜 Rules

- Snake 🐍 drinks Water 💧
- Water 💧 douses Gun 🔫
- Gun 🔫 kills Snake 🐍
- Same moves result in a Draw 🤝

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

Made as a beginner Python practice project. 🚀
