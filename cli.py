# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player


# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    current_player = "X"
    winner = None

    while winner == None:


        # Show the board to the user.
        for row in board:
            print(row)
            
        print("TODO: take a turn!")
        
        # Input a move from the player.
        while True:
            move = input(f"{current_player}'s turn. Enter your move (row,col): ")

            try:
                row, col = map(int, move.split(","))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == None:

                    board[row][col] = current_player # Update the board.
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter your move in the format row,col (e.g., 0,2).")

        # Check for a winner.
        winner = get_winner(board)

        # Update who's turn it is.
        current_player = other_player(current_player)


    print(f"Player {winner} wins!")

        

