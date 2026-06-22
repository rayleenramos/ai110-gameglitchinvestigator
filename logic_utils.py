def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# FIX: Refactored check_guess out of app.py into logic_utils.py with Claude in
# agent mode, separating game logic from the Streamlit UI.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: Corrected the swapped high/low hints (agent caught the bug, we fixed
    # it together) — a too-high guess now says LOWER and a too-low guess HIGHER.
    if guess > secret:
        # Guess is above the secret, so the player needs to go lower.
        return "Too High", "📉 Go LOWER!"
    else:
        # Guess is below the secret, so the player needs to go higher.
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
