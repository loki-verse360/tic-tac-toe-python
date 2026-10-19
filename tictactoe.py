import random
import os

# ANSI color codes for terminal styling
RED    = "\033[91m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_board(board):
    """Print the tic-tac-toe board with colors."""
    def color_cell(val):
        if val == "X":
            return f"{RED}{BOLD} X {RESET}"
        elif val == "O":
            return f"{BLUE}{BOLD} O {RESET}"
        else:
            return f"{CYAN} {val} {RESET}"

    print(f"\n{YELLOW}{BOLD}  === Tic-Tac-Toe ==={RESET}\n")
    for i in range(3):
        row = board[i * 3 : i * 3 + 3]
        print("  " + " | ".join(color_cell(c) for c in row))
        if i < 2:
            print(f"  {CYAN}-----+-----+-----{RESET}")
    print()

def check_winner(board, player):
    """Return True if the given player has won."""
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
        [0, 4, 8], [2, 4, 6],              # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def is_draw(board):
    """Return True if the board is full with no winner."""
    return all(cell in ("X", "O") for cell in board)

def get_empty_cells(board):
    """Return list of indices that are still empty."""
    return [i for i, cell in enumerate(board) if cell not in ("X", "O")]

def computer_move(board):
    """Easy AI: picks a completely random available cell."""
    return random.choice(get_empty_cells(board))

def get_human_move(board):
    """Prompt the human for a valid move (1-9)."""
    while True:
        try:
            move = int(input(f"  {GREEN}Your move (1-9): {RESET}")) - 1
            if move < 0 or move > 8:
                print(f"  {RED}Please enter a number between 1 and 9.{RESET}")
            elif move not in get_empty_cells(board):
                print(f"  {RED}That cell is already taken! Try another.{RESET}")
            else:
                return move
        except ValueError:
            print(f"  {RED}Invalid input. Please enter a number 1-9.{RESET}")

def play_game():
    """Run a single game of Tic-Tac-Toe."""
    # Board cells labeled 1-9 for display; replaced with X or O as game progresses
    board = [str(i + 1) for i in range(9)]

    clear()
    print(f"\n{YELLOW}{BOLD}  Welcome to Tic-Tac-Toe!{RESET}")
    print(f"  {CYAN}You are {RED}{BOLD}X{RESET}  |  {CYAN}Computer is {BLUE}{BOLD}O{RESET}")
    print(f"\n  {CYAN}Cell layout (enter the number to place your mark):{RESET}")
    print_board(board)
    input(f"  {CYAN}Press Enter to start...{RESET}")

    current_player = "X"   # Human always goes first

    while True:
        clear()
        print_board(board)

        if current_player == "X":
            print(f"  {GREEN}{BOLD}Your turn! (X){RESET}")
            move = get_human_move(board)
        else:
            print(f"  {BLUE}{BOLD}Computer is thinking...{RESET}")
            input(f"  {CYAN}(Press Enter to reveal the computer's move){RESET}")
            move = computer_move(board)
            print(f"  {BLUE}Computer chose cell {move + 1}.{RESET}")

        board[move] = current_player

        # Check game-over conditions
        if check_winner(board, current_player):
            clear()
            print_board(board)
            if current_player == "X":
                print(f"  {GREEN}{BOLD}*** You win! Congratulations! ***{RESET}\n")
            else:
                print(f"  {RED}{BOLD}*** Computer wins! Better luck next time. ***{RESET}\n")
            return

        if is_draw(board):
            clear()
            print_board(board)
            print(f"  {YELLOW}{BOLD}*** It's a draw! Well played! ***{RESET}\n")
            return

        # Alternate turns
        current_player = "O" if current_player == "X" else "X"

def main():
    """Main loop -- keep playing until the user quits."""
    while True:
        play_game()
        again = input(f"  {CYAN}Play again? (y/n): {RESET}").strip().lower()
        if again != "y":
            print(f"\n  {YELLOW}{BOLD}Thanks for playing! Goodbye :){RESET}\n")
            break

if __name__ == "__main__":
    main()
