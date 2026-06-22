from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" and tell the player to go LOWER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" and tell the player to go HIGHER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# FIX: Added this regression test with Claude in agent mode to lock in the
# high/low hint fix so the swapped-message bug can't silently come back.
def test_hint_direction_matches_guess():
    # Regression test for the high/low bug: the hint must point the player
    # toward the secret, never away from it.
    #
    # The original bug swapped the messages, so "Too High" told the player to
    # "Go HIGHER!" and "Too Low" told them to "Go LOWER!". These assertions
    # fail against that buggy version and pass against the fix.

    # Guess above the secret -> must say LOWER and must NOT say HIGHER.
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message

    # Guess below the secret -> must say HIGHER and must NOT say LOWER.
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message
