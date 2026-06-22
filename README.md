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

**Game Purpose:**
Glitchy Guesser is a number guessing game built with Streamlit where the player tries to guess a randomly chosen secret number within a limited number of attempts. The game gives higher/lower hints after each guess and tracks a score that rewards faster wins. The twist is that the starter code was intentionally shipped with 7 hidden bugs — the goal of the project was to find, document, and fix all of them.

**Bugs Found:**
1. Hints were backwards — "Go HIGHER" showed when the guess was too high, and "Go LOWER" when too low.
2. The range hint in the UI was hardcoded to "1 and 100" regardless of the selected difficulty.
3. The attempts counter started at 1 instead of 0, giving players one fewer guess than advertised.
4. Clicking "New Game" did not reset `status`, `score`, or `history`, causing "You already won" to appear immediately on the next game.
5. On even-numbered attempts, the secret number was cast to a string, so a correct integer guess could never match it.
6. Wrong guesses on even-numbered attempts awarded +5 points instead of deducting them.
7. Hard difficulty used range 1–50, which is narrower and easier than Normal's 1–100.

**Fixes Applied:**
1. Swapped the return messages in `check_guess()` so "Go LOWER" fires when `guess > secret`.
2. Replaced the hardcoded string in `st.info()` with the `low` and `high` variables.
3. Changed `st.session_state.attempts` initialization from `1` to `0`.
4. Added `st.session_state.status = "playing"`, `score = 0`, and `history = []` to the New Game handler.
5. Removed the even/odd branch that cast the secret to a string — `secret` is now always an integer.
6. Removed the `if attempt_number % 2 == 0: return current_score + 5` branch from `update_score()`.
7. Changed the Hard difficulty range from `1, 50` to `1, 500`.

## 📸 Demo Walkthrough

The following is a sample game played on Normal difficulty (range 1–100, 8 attempts allowed). The secret number is 63.

1. Game loads — sidebar shows "Range: 1 to 100" and "Attempts allowed: 8". The hint bar reads "Guess a number between 1 and 100. Attempts left: 8".
2. Player enters **40** and clicks Submit → hint shows **"Go HIGHER"**. Attempts left: 7. Score: -5.
3. Player enters **75** → hint shows **"Go LOWER"**. Attempts left: 6. Score: -10.
4. Player enters **60** → hint shows **"Go HIGHER"**. Attempts left: 5. Score: -15.
5. Player enters **68** → hint shows **"Go LOWER"**. Attempts left: 4. Score: -20.
6. Player enters **63** → balloons appear, game shows **"You won! The secret was 63. Final score: 30"**. Status is set to "won".
7. Player clicks **New Game** → attempts reset to 0, secret regenerates, status resets to "playing", score resets to 0. A fresh game begins immediately with no "You already won" message.

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
