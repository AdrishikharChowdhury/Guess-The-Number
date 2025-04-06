# ✅ TODO.md – Guess The Number 🎯

A fun number-guessing game with single and two-player modes. This file outlines everything that needs to be done (or improved) to make this project more robust, modular, and extensible.

---

## 🔹 1. Core Features

- [x] Implement basic single-player gameplay loop  
- [x] Implement two-player mode with alternating turns  
- [x] Set a random target number using `random.randint()`  
- [x] Allow custom difficulty settings (Easy, Medium, Hard, Nightmare)  
- [x] Handle incorrect input with try-except blocks  
- [x] Allow quitting the game mid-way with `"quit"`  
- [x] Show how many turns are left  
- [x] Use `match-case` (Python 3.10+) for choices

---

## 🧱 2. Code Structure & Modularization

- [x] Split code into functions for reusability  
- [x] Create a separate `get_valid_input()` function  
- [x] Keep `main()` function clean and readable  
- [ ] Separate modules (optional):
  - [ ] `input_utils.py` → input validation and utility methods
  - [ ] `game_modes.py` → single and two-player logic
  - [ ] `config.py` → constants, difficulty ranges
  - [ ] `guesser.py` → core game logic and result evaluation
- [ ] Create a `__main__.py` or CLI entry point (for packaging)

---

## 💡 3. User Interface Enhancements (CLI)

- [ ] Add colorized output (e.g., using `colorama`)
- [ ] Add a scoreboard or turn summary at the end
- [ ] Animate or pause briefly on winning or quitting (e.g., using `time.sleep`)
- [ ] Use ASCII art for welcome screen or game over
- [ ] Clear screen between turns (e.g., `os.system("cls" or "clear")`)

---

## 🧪 4. Testing

- [ ] Add basic unit tests using `unittest` or `pytest`:
  - [ ] Test guesser logic
  - [ ] Test input validation
  - [ ] Test game loop control (turn countdown, quit)
- [ ] Use mock inputs to simulate user behavior in tests
- [ ] Ensure test coverage > 90%

---

## 📦 5. Packaging

- [ ] Create `requirements.txt`
- [ ] Add a `setup.py` or `pyproject.toml` for packaging
- [ ] Structure folders properly (`src/`, `tests/`, `assets/`, etc.)
- [ ] Add `README.md` with game instructions
- [ ] Add `LICENSE` file

---

## 🌐 6. Optional Web Version (Flask)

> **Stretch goal to move your project from CLI to Web App.**

- [ ] Set up Flask application (`app.py`)
- [ ] Create HTML templates (Jinja2) for:
  - [ ] Welcome screen
  - [ ] Input form (guess)
  - [ ] Result display
  - [ ] Game over screen
- [ ] Use sessions to store player state
- [ ] Use Bootstrap or Tailwind for styling
- [ ] Deploy on Render/Heroku or GitHub Pages (for frontend only)
- [ ] Add a `/api` route to allow AJAX-based guessing

---

## 🎮 7. Additional Game Features

- [ ] Add time limit per turn (optional challenge)
- [ ] Track and display all guesses per player
- [ ] Add difficulty-based scoring system
- [ ] Support infinite mode (until player wins)
- [ ] Enable dynamic difficulty scaling (based on player performance)
- [ ] Show a leaderboard (local file or JSON storage)

---

## 🔐 8. Save and Load Game State

- [ ] Save game state (turns left, guesses) to a file
- [ ] Add option to resume a previous game
- [ ] Store game history for players (e.g., using JSON or Pickle)

---

## 🎯 9. AI Opponent (Advanced Fun Feature)

- [ ] Implement a bot opponent using basic number guessing strategy
- [ ] Use binary search logic for AI guesses
- [ ] Add AI difficulty level (Easy = random, Hard = optimal)

---

## 🧠 10. Improvements & Optimization

- [ ] Improve code readability and use better naming conventions
- [ ] Remove duplicate logic (DRY principle)
- [ ] Document all functions using proper docstrings
- [ ] Use logging module for debug and error logs

---

## 📝 11. Documentation

- [ ] Expand `README.md` with:
  - [ ] Game rules
  - [ ] Difficulty levels explanation
  - [ ] CLI instructions
  - [ ] Screenshots (optional)
- [ ] Add inline comments for logic explanation
- [ ] Include a changelog

---

Let me know if you want a version of this in a markdown file or want to move on to the **Quiz TODO.md** next!