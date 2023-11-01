# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
#check row
    for row in board:
        if row[0] is not None and len(set(row)) == 1:
            return row[0]
#check column
    for i in range(len(board)):
        column = [board[j][i] for j in range(len(board))]
        if column[0] is not None and len(set(column)) == 1:
            return column[0]
#check diagonals
    top_left_to_bottom_right = [board[i][i] for i in range(len(board))]
    if top_left_to_bottom_right[0] is not None and len(set(top_left_to_bottom_right)) == 1:
        return board[i][i]

    top_right_to_bottom_left = [board[i][len(board)-i-1] for i in range(len(board))]
    if top_right_to_bottom_left[0] is not None and len(set(top_right_to_bottom_left)) == 1:
        return board[0][range(board)-1]    
    return None  


def other_player(player):
    if player == "X":
        return "O"
    elif player == "O":
        return "X"
    else:
        raise ValueError("Invalid player character")

