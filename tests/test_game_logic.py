from logic_utils import check_guess, update_score, get_range_for_difficulty

# ── Existing starter tests (fixed to unpack the returned tuple) ──────────────

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# ── Bug fix: hints were backwards ─────────────────────────────────────────────

def test_too_high_shows_go_lower():
    # guess > secret should tell the player to go LOWER, not HIGHER
    _, message = check_guess(60, 40)
    assert "LOWER" in message

def test_too_low_shows_go_higher():
    # guess < secret should tell the player to go HIGHER, not LOWER
    _, message = check_guess(20, 40)
    assert "HIGHER" in message


# ── Bug fix: wrong guess should never award points ────────────────────────────

def test_too_high_deducts_points():
    # "Too High" on an even attempt used to give +5 — now it should always deduct
    new_score = update_score(100, "Too High", 2)
    assert new_score == 95

def test_too_high_odd_attempt_deducts_points():
    new_score = update_score(100, "Too High", 3)
    assert new_score == 95

def test_too_low_deducts_points():
    new_score = update_score(100, "Too Low", 1)
    assert new_score == 95


# ── Bug fix: Hard difficulty range must be wider than Normal ──────────────────

def test_hard_range_wider_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_easy_range_narrower_than_normal():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high


# ── Bug fix: correct integer guess must always register as a win ──────────────

def test_correct_guess_always_wins():
    # Previously, on even attempts the secret was cast to str so 42 != "42"
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"

def test_correct_guess_is_not_too_high_or_too_low():
    outcome, _ = check_guess(99, 99)
    assert outcome not in ("Too High", "Too Low")
