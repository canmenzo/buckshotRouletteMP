# 🔫 Buckshot Roulette MP

[![license](https://img.shields.io/github/license/canmenzo/buckshotRouletteMP)](LICENSE) ![python](https://img.shields.io/badge/python-3.6+-blue?logo=python&logoColor=white) ![runs in](https://img.shields.io/badge/runs%20in-terminal-4D4D4D?logo=gnometerminal&logoColor=white)

A small terminal game for two players on the same keyboard, loosely based on [Buckshot Roulette](https://store.steampowered.com/app/2835570/Buckshot_Roulette/). Single Python file, no dependencies.

### ✨ Features
- 👥 Two players take turns in one terminal (hot seat)
- ❤️ Each player starts with 3 HP
- 🎲 The shotgun holds 6 shells, 1 to 5 of them live, shuffled; the live/blank count is announced on every reload
- 🎯 On your turn, shoot your opponent or yourself; a blank on yourself keeps your turn
- 🔄 The shotgun reloads automatically when empty; the game ends when a player reaches 0 HP

### 🚀 Quick start
```bash
git clone https://github.com/canmenzo/buckshotRouletteMP.git
cd buckshotRouletteMP
python3 game.py
```
Enter both player names, then type `1` (shoot opponent) or `2` (shoot yourself) each turn.

### 📄 License
MIT
