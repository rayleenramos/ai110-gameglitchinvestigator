# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.** It's a number-guessing game built with Streamlit. The app picks a secret number within a range based on difficulty (Easy 1–20, Normal 1–100, Hard 1–50), and the player tries to guess it within a limited number of attempts. After each guess the game gives a hint ("Too High" / "Too Low") and updates the score, ending when the player guesses correctly or runs out of attempts.

- [x] **Detail which bugs you found.**
  - **Swapped high/low hints:** `check_guess` told the player to "Go HIGHER!" when their guess was already too high, and "Go LOWER!" when it was too low, the hints pointed the wrong way.
  - **Logic mixed with UI:** the core game logic (`check_guess`) lived directly in `app.py` alongside the Streamlit UI code, making it hard to test in isolation.

- [x] **Explain what fixes you applied.**
  - Corrected the swapped hints so a too-high guess now says "Go LOWER!" and a too-low guess says "Go HIGHER!".
  - Refactored `check_guess` out of `app.py` into `logic_utils.py` and imported it back, separating game logic from the UI.
  - Added a regression test (`test_hint_direction_matches_guess`) that fails against the old buggy code and passes against the fix, so the bug can't silently return.

## 📸 Demo Walkthrough

A text-based record of how the fixed game behaves end-to-end, so a reader can follow along without running it. (Sample game on **Normal** difficulty, range 1–100, secret number = **63**.)

1. The player opens the app, sees "Guess a number between 1 and 100," and enters a guess of **40**.
2. The game returns **"Too Low"** with the hint **"📈 Go HIGHER!"** — correctly pointing the player upward.
3. The player enters a guess of **70** → the game returns **"Too High"** with the hint **"📉 Go LOWER!"** — correctly pointing the player downward.
4. The score updates after each guess, and the "Attempts left" counter decreases by one per submission.
5. The player enters **63**, the game shows **"🎉 Correct!"**, celebrates with balloons, reveals the secret number, displays the final score, and ends the game until "New Game" is clicked.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

Challenge 1: Advanced Edge-Case Testing — pytest output:

```
$ python -m pytest tests/ -v
============================= test session starts ==============================
platform darwin -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
cachedir: .pytest_cache
rootdir: /Users/rayleenramos/Desktop/AI_110/ai110-gameglitchinvestigator
plugins: anyio-4.13.0
collecting ... collected 4 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 25%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 50%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 75%]
tests/test_game_logic.py::test_hint_direction_matches_guess PASSED       [100%]

============================== 4 passed in 0.05s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
