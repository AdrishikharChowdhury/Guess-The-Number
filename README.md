# 🎯 Number Guessing Game

The **Number Guessing Game** is a console-based Python game designed for both **single-player** and **two-player** modes. The goal is simple: guess a randomly generated number within a given number of attempts. With varying difficulty levels and a turn-based system, this game blends logic, suspense, and a little bit of luck into a fun coding project or casual challenge.

---

## 🧩 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [How to Play](#how-to-play)
- [Game Modes](#game-modes)
- [Difficulty Levels](#difficulty-levels)
- [How to Run](#how-to-run)
- [Code Structure](#code-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 📘 About the Project

This game was built as a fun way to sharpen Python programming skills while demonstrating concepts like:

- Modular function-based programming
- Input validation and user interaction
- Conditional logic and control flow
- Use of `match-case` (Python 3.10+)
- Turn-based gameplay and looping mechanics

It's a lightweight, interactive, text-based game that’s ideal for beginners looking to understand how to build logic-driven applications.

---

## ✅ Features

- 🎮 **Single Player Mode** — Play against the computer and try to guess the hidden number.
- 🤝 **Two Player Mode** — Compete with a friend by guessing the number turn-by-turn.
- 🔢 **Four Difficulty Levels** — Easy to Nightmare, each with its own number range and limited turns.
- 🔄 **Replayable Design** — Each session generates a new random number.
- 🚫 **Quit Anytime** — Players can type `quit` to exit mid-game.
- ⚠️ **Robust Input Handling** — Prevents crashes from invalid input using error catching.

---

## 🎮 How to Play

1. Choose your **difficulty level**.
2. Select a **game mode** (single-player or two-player).
3. Start guessing numbers within the range specified by the difficulty.
4. Each incorrect guess gives you a hint — "Too small" or "Too big".
5. Guess correctly within the allowed number of turns to win.
6. If playing with a friend, take alternate turns until someone wins or both run out of turns.

---

## 🕹️ Game Modes

### 1. Single Player
- One user plays against a randomly generated number.
- Hints are provided to guide the player after each incorrect guess.

### 2. Two Player
- Two players take turns guessing the same number.
- If one player guesses correctly, they win and the other loses.
- A player can also type `quit` to forfeit the game.

---

## 🔧 Difficulty Levels

Each difficulty level changes the guessing range and number of turns:

| Difficulty  | Range     | Turns |
|-------------|-----------|-------|
| Easy        | 1 - 50    | 15    |
| Medium      | 1 - 100   | 12    |
| Hard        | 1 - 500   | 10    |
| Nightmare   | 1 - 1000  | 8     |

---

## 🚀 How to Run the Game

Make sure you have Python 3.10 or newer installed (for `match-case` syntax).

### Run from terminal/command prompt:

```bash
python guessing_game.py
```

Follow the prompts in the terminal to start the game.

---

## 🗂️ Code Structure

```
guessing_game.py
README.md
```

### Key Functions:

- `get_valid_input(prompt)`: Handles user input and catches invalid entries.
- `guesser(name, x, target)`: Checks the guess against the target number.
- `single_player(turns, target)`: Manages the logic for single-player mode.
- `two_player(turns, target)`: Manages the logic for two-player mode.
- `difficulty()`: Allows the user to choose a difficulty setting.
- `choose_game_mode()`: Prompts the user to select a game mode.
- `main()`: The entry point that connects all components.

---

## 🔮 Future Enhancements

Here are some ideas to extend the functionality:

- ✅ Add a replay option after each game
- 🧠 Add a "Hint Mode" to give smarter clues (e.g., "Very close!")
- 📝 Store high scores and player history
- 🌐 Create a web-based version using Flask or Django
- 🖼️ Develop a GUI using Tkinter or PyQt
- 🌍 Multiplayer over network (basic socket programming)

---

## 🤝 Contributing

Feel free to fork the project and make improvements! If you find bugs, have ideas, or want to collaborate:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open-source and free to use for educational and personal purposes. No restrictions apply.

---

**Made with 💻 + ❤️ in Python. Enjoy the game and happy guessing!**
