# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it loaded and let me type a guess, but several things immediately felt wrong. The hints were backwards — when I guessed too high, it told me to "Go HIGHER!" instead of lower. After winning once, clicking "New Game" did not actually restart the game; it still showed "You already won" and blocked all input, so I had to reload the browser to play again. The attempts counter also started at 7 instead of 8, and the info bar always said "between 1 and 100" even on Easy mode (which is 1–20).

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 60 (secret is 40) | Hint says "Go LOWER!" because 60 > 40 | Hint says "Go HIGHER!" — directions are flipped | None |
| Click "New Game" after winning | Game resets fully and lets me play again | Still shows "You already won. Start a new game to play again." — input is blocked | None |
| First load of the game on Normal difficulty (8 attempts) | Info banner shows "Attempts left: 8" | Shows "Attempts left: 7" — counter starts at 1 instead of 0 | None |
| Switch difficulty to Easy | Info banner updates to "Guess a number between 1 and 20" | Banner always shows "Guess a number between 1 and 100" regardless of difficulty | None |

---

## 2. How did you use AI as a teammate?

I used Claude Code (VS Code extension) as my AI coding assistant throughout this project.

**Correct suggestion:** I told the AI the hints were backwards and it correctly traced the root cause to lines 158–163 in app.py, where the code was alternating between passing `str(secret)` and `int(secret)` on every other attempt. Because comparing an int to a string raises a `TypeError` in Python 3, the `check_guess` fallback path ran, which did lexicographic string comparison and flipped the direction. The AI suggested removing those three lines and always passing `st.session_state.secret` directly as an integer. I verified this fix by running `pytest tests/test_game_logic.py -v` and all hint-direction tests passed, then also confirmed in the live game that guessing 60 when the secret was 40 now correctly showed "Go LOWER!".

**Incorrect / misleading suggestion:** Early on, when I said I had already fixed the backwards hints bug, the AI initially accepted that and moved on — but the code was actually unchanged. When it re-read `app.py` it caught its own mistake and told me the bug was still present. This was a reminder that I cannot just tell the AI something is fixed; it (and I) need to actually read the code and verify. I confirmed by looking at lines 158–163 myself and seeing the string alternation was still there before the AI's final fix.

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed in two ways: first by reading the diff of the changed code to confirm the root cause was removed, and second by running the test suite with `pytest tests/test_game_logic.py -v` to get a pass/fail signal.

The most useful test I ran was the full suite after the refactor, which returned `6 passed in 0.01s`. Three of those tests were new ones the AI helped design specifically targeting the hint direction bug — `test_too_high_message_says_go_lower`, `test_too_low_message_says_go_higher`, and `test_hint_direction_not_flipped`. Each checks not just the outcome string ("Too High") but also the actual message text ("LOWER" / "HIGHER"), which is the part the original bug got wrong.

The AI helped me design those tests by explaining that checking only the outcome label is not enough — you also need to assert the message content, since the original code returned the right outcome label but the wrong direction word. That distinction helped me understand what the test should actually verify versus what the existing tests were missing.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
