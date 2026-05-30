import random


def get_lives(difficulty: str) -> int:
    """Return lives based on difficulty string."""
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        raise ValueError(f"Unknown difficulty: {difficulty!r}")


def check_guess(guess: int, number: int) -> str:
    """Compare guess to the secret number. Returns 'high', 'low', or 'correct'."""
    if guess > number:
        return "high"
    elif guess < number:
        return "low"
    else:
        return "correct"


def play_game(number: int, difficulty: str, input_fn=input, print_fn=print) -> str:
    """
    Run one full game.
    Returns 'win' or 'lose'.
    input_fn / print_fn are injectable for testing.
    """
    lives = get_lives(difficulty)
    game_over = False

    while lives > 0 and not game_over:
        print_fn(f"You have {lives} attempts to guess the number.")
        guess = int(input_fn("Make a guess: "))
        result = check_guess(guess, number)

        if result == "high":
            print_fn("Too high!")
        elif result == "low":
            print_fn("Too low!")
        else:
            print_fn("You guessed right — you win!")
            game_over = True
            return "win"

        lives -= 1

    print_fn(f"You lose! The number was {number}.")
    return "lose"