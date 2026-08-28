from random import choice

# List of possible moves
MOVES = (0, 1, 2)
MOVE_MAP = {0: "Snake", 1: "Water", 2: "Gun"}


# ANSI colour codes
class Colour:
    GREEN = "\033[92m"  # win
    RED = "\033[91m"  # lose
    YELLOW = "\033[93m"  # draw
    RESET = "\033[0m"


# 2d List for storing results
RESULT_TABLE = [
["D", "W", "L"], 
["L", "D", "W"], 
["W", "L", "D"]
]

# dictionary for mapping the results (coloured)
RESULT_MAP = {
    "W": f"{Colour.GREEN}You win{Colour.RESET}",
    "L": f"{Colour.RED}You lose{Colour.RESET}",
    "D": f"{Colour.YELLOW}It's a draw{Colour.RESET}",
}


def get_max_rounds():
    """This func take the max rounds form player with error robustness"""
    while True:
        try:
            max_rounds = int(input("Enter the max rounds you wanna play: "))
            if max_rounds <= 0:
                raise ValueError
            return max_rounds
        except ValueError:
            print("INVALID INPUT!")


def get_computer_move():
    """Returns a random move from the list of possible moves."""
    return choice(MOVES)


def get_result_msg(result):
    """this func map the result with dict and return message"""
    return RESULT_MAP[result]


def get_player_move():
    """This function takes player input with error robustness"""
    while True:
        try:
            player_move = int(
                input(
                    "\n0. Snake \n1. Water \n2. Gun \nChoose Your Move: \n0 or 1 or 2\n"
                )
            )

            if player_move not in MOVES:
                raise ValueError

            return player_move  # ✅ only valid input returns

        except ValueError:
            print("Invalid input,\n enter a number between 0, 1 or 2 \n\n TRY AGAIN!")


def update_score(player_score, computer_score, draws, result):
    """this func updates score using local variable and tuple unpacking"""
    match result:
        case "W":
            player_score += 1
        case "L":
            computer_score += 1
        case "D":
            draws += 1
            

    return player_score, computer_score, draws


def calculate_win_percentage(player_score, max_rounds):
    return (player_score / max_rounds) * 100
    
    
def final_score(player_score, computer_score, draws):
    """this func return final score as f-string"""
    return f"\nPlayer: {player_score} \nComputer: {computer_score} \nDraws: {draws}"


def final_result(player_score, computer_score):
    """this func return final result"""
    if player_score == computer_score:
        return f"FINAL RESULT: \n{Colour.YELLOW}ITS A DRAW{Colour.RESET}"
    elif player_score > computer_score:
        return f"FINAL RESULT: \n{Colour.GREEN}YOU WIN{Colour.RESET}"
    elif player_score < computer_score:
        return f"FINAL RESULT: \n{Colour.RED}YOU LOSE{Colour.RESET}"


def game():
    """run main game"""
    player_score = 0
    computer_score = 0
    draws = 0
    rounds = 0
    max_rounds = get_max_rounds()
    while rounds < max_rounds:
        player_move = get_player_move()
        computer_move = get_computer_move()
        print("-" * 20)
        print(
            f"Your move is {MOVE_MAP[player_move]} \nComputer move is {MOVE_MAP[computer_move]}"
        )
        result = RESULT_TABLE[player_move][computer_move]
        print(get_result_msg(result))
        player_score, computer_score, draws = update_score(
            player_score, computer_score, draws, result
        )
        rounds += 1
        print("-" * 20)

    # End of loop
    win_percentage = calculate_win_percentage(player_score, max_rounds)
    score_final = final_score(player_score, computer_score, draws)
    result_final = final_result(player_score, computer_score)
    
    print(score_final)
    print(f"Win % : {win_percentage:.2f}")
    print(result_final)
    
    return player_score, computer_score, draws


def get_again():
    while True:
        try:
            again = input("Another game? (y/n)").strip().lower()
            if again not in ["y", "n"]:
                raise ValueError   
            return again
        except ValueError:
            print("INVALID INPUT!")
        

def main():
    while True:
        game()
        again = get_again()
        if again != "y":
            break
        

        

if __name__ == "__main__":
    main()
