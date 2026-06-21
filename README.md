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

**Game purpose:** A number guessing game built with Streamlit where the player tries to guess a secret number within a limited number of attempts. The difficulty setting controls the number range (Easy: 1–20, Normal: 1–100, Hard: 1–50) and attempt limit.

**Bugs found:**
1. Hints were backwards — guessing too high showed "Go HIGHER!" instead of "Go LOWER!" (caused by alternating `str(secret)` on even attempts, triggering a bad string comparison fallback)
2. "New Game" button did not reset `status`, `score`, or `history` — the game stayed in a "won" state and blocked all input
3. Info banner always showed "between 1 and 100" regardless of difficulty (hardcoded instead of using the `low`/`high` variables)

**Fixes applied:**
1. Removed the `str(secret)` alternation — `check_guess` now always receives two integers
2. Added `status`, `score`, and `history` resets to the New Game handler
3. Changed the info banner to use `{low}` and `{high}` dynamically
4. Refactored `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` out of `app.py` and into `logic_utils.py`

## 📸 Demo Walkthrough

1. Player opens the app on **Normal** difficulty (1–100, 8 attempts). The info banner correctly shows "Guess a number between 1 and 100. Attempts left: 8".
2. Player enters **50** and clicks Submit → hint shows "📈 Go HIGHER!" meaning the secret is above 50. Attempts left drops to 7.
3. Player enters **75** → hint shows "📉 Go LOWER!" meaning the secret is between 50 and 75. Attempts left: 6.
4. Player enters **62** → "📈 Go HIGHER!". Attempts left: 5.
5. Player enters **68** → "📉 Go LOWER!". Attempts left: 4.
6. Player enters **65** → "🎉 Correct!" — balloons appear, score displayed, game status set to "won".
7. Player clicks **New Game** → game fully resets (attempts back to 8, new secret generated, score cleared) and is immediately playable again.

## 🧪 Test Results

```
(AIvenv) fatimahhassan@Fatimahs-MBP ai110-module1show-gameglitchinvestigator-starter % python -m pytest
====================================================== test session starts =======================================================
platform darwin -- Python 3.13.0, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/fatimahhassan/Documents/CodePath/AI_110/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 6 items

tests/test_game_logic.py ......                                                                                            [100%]

======================================================= 6 passed in 0.01s ========================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
