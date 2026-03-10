from logic_utils import check_guess, parse_guess


# --- Existing tests (fixed: check_guess returns a tuple) ---
# The AI generated tests that compared result == 'Win' directly.
# I realised check_guess returns a (outcome, message) tuple and unpacked it.

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: Swapped hint messages ---
# I wrote these tests after noticing the hint pointed the wrong way during play.
# AI helped me pin down the exact assert wording once I described the expected output.
# Before fix: "Too High" returned "📈 Go HIGHER!" and "Too Low" returned "📉 Go LOWER!"

def test_too_high_message_says_go_lower():
    """Hint for a high guess must tell the player to go LOWER, not HIGHER."""
    outcome, message = check_guess(99, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_message_says_go_higher():
    """Hint for a low guess must tell the player to go HIGHER, not LOWER."""
    outcome, message = check_guess(1, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- Bug 2: String coercion causing wrong lexicographic comparison ---
# I found this bug using the debug expander: 9 vs 10 kept returning 'Too High'.
# AI explained the lexicographic trap and helped me write the reproducer test.
# Before fix: on even attempts secret was str(secret), so check_guess(9, "10")
# entered the TypeError branch where str(9)="9" > "10" lexicographically → "Too High"
# even though 9 < 10.

def test_single_digit_vs_double_digit_int_comparison():
    """9 is less than 10; must return Too Low, not Too High (lexicographic trap)."""
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low", f"Expected Too Low but got {outcome}"


def test_string_coerced_secret_gives_wrong_result():
    """
    Reproduces the pre-fix bug: when secret was accidentally str'd,
    check_guess(9, '10') landed in the TypeError branch and compared
    '9' > '10' which is True, returning 'Too High' instead of 'Too Low'.
    This test documents that the function must NOT be called with a str secret.
    """
    # With str secret, the result is wrong — this is the bug scenario
    outcome_buggy, _ = check_guess(9, "10")
    assert outcome_buggy == "Too High", (
        "This reproduces the pre-fix behaviour: lexicographic '9'>'10' is True"
    )
    # With int secret (the fix), the result is correct
    outcome_fixed, _ = check_guess(9, 10)
    assert outcome_fixed == "Too Low", (
        "With an int secret the comparison is numeric and correct"
    )


# --- parse_guess edge cases ---

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert not ok
    assert err == "Enter a guess."


def test_parse_none():
    ok, value, err = parse_guess(None)
    assert not ok
    assert err == "Enter a guess."


def test_parse_non_numeric():
    ok, value, err = parse_guess("abc")
    assert not ok
    assert err == "That is not a number."


def test_parse_float_string_truncates():
    ok, value, err = parse_guess("7.9")
    assert ok
    assert value == 7


def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok
    assert value == 42
    assert err is None
