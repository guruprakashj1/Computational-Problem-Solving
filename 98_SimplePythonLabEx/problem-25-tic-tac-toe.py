# Problem 25: Implement a simple Tic-Tac-Toe game using loops and conditional statements

"""
Explanation: This problem uses loops and conditional statements to create a simple Tic-Tac-Toe game.
Logic: Represent the board as a list, take turns for each player, check for win conditions after each move.
Algorithm:
1. Initialize an empty 3x3 board
2. Repeat until the game is over:
   a. Display the current board
   b. Get the current player's move
   c. Update the board with the move
   d. Check if the current player has won
   e. Check if the board is full (draw)
   f. Switch to the other player
3. Display the final board and game result
"""

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That cell is already occupied. Try again.")

play_tic_tac_toe()
