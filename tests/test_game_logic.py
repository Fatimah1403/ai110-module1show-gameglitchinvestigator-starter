from logic_utils import check_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix tests: backwards hints ---
# Root cause: app.py was passing str(secret) on even attempts, triggering a
# TypeError fallback that did lexicographic string comparison and flipped the
# direction. Fix: always pass secret as int. These tests lock in correct direction.

def test_too_high_message_says_go_lower():
    # Guess 60, secret 50 → player guessed too HIGH → must say "Go LOWER"
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message, f"Expected 'Go LOWER' but got: {message}"

def test_too_low_message_says_go_higher():
    # Guess 40, secret 50 → player guessed too LOW → must say "Go HIGHER"
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message, f"Expected 'Go HIGHER' but got: {message}"

def test_hint_direction_not_flipped():
    # Explicitly confirm the two directions are never swapped
    _, msg_high = check_guess(90, 10)
    _, msg_low = check_guess(10, 90)
    assert "LOWER" in msg_high
    assert "HIGHER" in msg_low
