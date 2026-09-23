from random import choice

MOVES = (0, 1, 2)

MOVE_MAP = {
    0: "Snake",
    1: "Water",
    2: "Gun"
}

RESULT_TABLE = [
    ["D", "W", "L"],
    ["L", "D", "W"],
    ["W", "L", "D"]
]


def get_computer_move():
    """Returns a random move from the list of possible moves."""
    return choice(MOVES)


def get_result(player_move, computer_move):
    """Determines the result of a round."""
    return RESULT_TABLE[player_move][computer_move]


def update_score(player_score, computer_score, draws, result):
    """Updates the scores based on the round result."""
    match result:
        case "W":
            player_score += 1
        case "L":
            computer_score += 1
        case "D":
            draws += 1

    return player_score, computer_score, draws


def calculate_round_win_percentage(player_score, max_rounds):
    """Return the percentage of rounds won by the player."""
    return (player_score / max_rounds) * 100


def final_result(player_score, computer_score):
    """Determines the final game result."""
    if player_score == computer_score:
        return "D"
    elif player_score > computer_score:
        return "W"
    else:
        return "L"
