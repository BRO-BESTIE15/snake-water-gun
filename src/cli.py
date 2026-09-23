import engine


# ANSI colour codes
class Colour:
    GREEN = "\033[92m"  # win
    RED = "\033[91m"  # lose
    YELLOW = "\033[93m"  # draw
    RESET = "\033[0m"
    CYAN = "\033[96m"


RESULT_MAP = {
    "W": f"{Colour.GREEN}You win{Colour.RESET}",
    "L": f"{Colour.RED}You lose{Colour.RESET}",
    "D": f"{Colour.YELLOW}It's a draw{Colour.RESET}",
}


def get_max_rounds():
    """Ask how many rounds to play and validate the answer."""
    while True:
        try:
            max_rounds = int(input("How many rounds would you like to play? "))
            if max_rounds <= 0:
                raise ValueError
            return max_rounds
        except ValueError:
            print("INVALID INPUT!")


def get_result_msg(result):
    """Return the display message for a round result."""
    return RESULT_MAP[result]


def get_player_move():
    while True:
        try:
            print(
                f" {Colour.CYAN}\tChoose your move:{Colour.RESET}\n"
                " \t0 → 🐍 Snake\n \t1 → 💧 Water\n \t2 → 🔫 Gun"
            )

            player_move = int(input("Your choice: "))

            if player_move not in engine.MOVES:
                raise ValueError

            return player_move

        except ValueError:
            print(f"{Colour.RED}❌ Please enter 0, 1, or 2.{Colour.RESET}")


def final_score(player_score, computer_score, draws):
    """Format the final round scores."""
    return (
        f"{Colour.CYAN}Player: {player_score}{Colour.RESET} \n"
        f"{Colour.RED}Computer: {computer_score}{Colour.RESET} \n"
        f"{Colour.YELLOW}Draws: {draws}{Colour.RESET}"
    )


def show_title():
    print(f"{Colour.CYAN} \n|| 🐍 SNAKE WATER GUN 🔫 ||  \n{Colour.RESET}")


def separator():
    print(f"{Colour.CYAN}{'═' * 35}{Colour.RESET}")


def display_final_result(result):
    if result == "D":
        return f"FINAL RESULT: \n{Colour.YELLOW}ITS A DRAW{Colour.RESET}"
    elif result == "W":
        return f"FINAL RESULT: \n{Colour.GREEN}YOU WIN{Colour.RESET}"
    elif result == "L":
        return f"FINAL RESULT: \n{Colour.RED}YOU LOSE{Colour.RESET}"


def game():
    """Run one game and return its round totals."""
    player_score = 0
    computer_score = 0
    draws = 0
    rounds = 0
    max_rounds = get_max_rounds()
    while rounds < max_rounds:
        print(f"\n{Colour.CYAN}══════════ ROUND {rounds + 1} ══════════{Colour.RESET}")
        player_move = get_player_move()
        computer_move = engine.get_computer_move()
        separator()

        print(
            f"Your move is {engine.MOVE_MAP[player_move]}\n"
            f"Computer move is {engine.MOVE_MAP[computer_move]}"
        )
        result = engine.get_result(player_move, computer_move)
        print(get_result_msg(result))
        player_score, computer_score, draws = engine.update_score(
            player_score, computer_score, draws, result
        )
        print(
            f"\nScore → You: {player_score} | "
            f"Computer: {computer_score} | "
            f"Draws: {draws}"
        )
        rounds += 1
        separator()

    # End of loop
    round_win_percentage = engine.calculate_round_win_percentage(
        player_score, max_rounds
    )
    score_final = final_score(player_score, computer_score, draws)
    result_final = engine.final_result(player_score, computer_score)
    print(f"Round win % :{Colour.CYAN} {round_win_percentage:.2f} {Colour.RESET}")
    print(score_final)
    separator()
    print(display_final_result(result_final))

    return player_score, computer_score, draws


def get_again():
    while True:
        try:
            again = input("Another game? (y/n)").strip().lower()
            if again not in ("y", "n"):
                raise ValueError
            return again
        except ValueError:
            print("INVALID INPUT!")


def main():
    show_title()
    while True:
        game()
        again = get_again()
        if again != "y":
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()
