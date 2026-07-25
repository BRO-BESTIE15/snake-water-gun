# 🐍 Snake Water Gun Game
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Beginner](https://img.shields.io/badge/Level-Beginner-orange)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)

A simple **Snake 🐍, Water 💧, Gun 🔫** game made in Python.

📄 **Source Code:** [`s-w-g-v2.py`](s-w-g-v2.py)

Play **Snake, Water, Gun** against the computer! Before the game starts, you can choose how many rounds you want to play. The computer randomly selects its moves, and the winner of each round is decided using a lookup table. At the end, the final scores are compared to declare the overall winner.

## ✨ Features

- 🎲 Random computer moves
- 🎮 User-configurable number of rounds
- ✅ Input validation
- 📊 Live score tracking
- 🏆 Final winner announcement
- 🧠 Lookup table-based game logic

## 🚀 How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Run the program:

```bash
python s-w-g-v2.py
```

## 🎮 Controls

| Input | Move |
|------:|------|
| `0` | 🐍 Snake |
| `1` | 💧 Water |
| `2` | 🔫 Gun |

First, enter the number of rounds you want to play. Then, enter the number corresponding to your move when prompted.

## 📷 Example

```text
Enter the max rounds you wanna play: 2

 0. Snake
 1. Water
 2. Gun
 Choose Your Move:
 0 or 1 or 2
1
--------------------
Your move is Water
Computer move is Water
It's a draw
--------------------

 0. Snake
 1. Water
 2. Gun
 Choose Your Move:
 0 or 1 or 2
0
--------------------
Your move is Snake
Computer move is Snake
It's a draw
--------------------
FINAL RESULT:
ITS A DRAW

```

## 📚 Concepts Used

- Functions
- Lists
- 2D Lists (Lookup Table)
- Dictionaries
- `random.choice()`
- Loops
- Input Validation (`try`/`except`)
- Variables and Score Keeping

## 📜 Rules

- Snake 🐍 drinks Water 💧
- Water 💧 douses Gun 🔫
- Gun 🔫 kills Snake 🐍
- Same moves result in a Draw 🤝

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

Made as a beginner Python practice project. 🚀