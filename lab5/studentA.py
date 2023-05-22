from enum import Enum
from typing import List


class Move(Enum):
    X = 1
    O = 2
    EMPTY = 0


def new_board(size=3):
    board = []
    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(Move.EMPTY)

        board.append(row)

    return board


def is_game_over(board) -> (bool, Move):
    output = _check_horizontal(board)
    if output != Move.EMPTY:
        return True

    output = _check_vertical(board)
    if output != Move.EMPTY:
        return True

    output = _check_diagonal(board)
    if output != Move.EMPTY:
        return True

    return _check_board_full(board)


def announce_outcome(board):
    output = _check_diagonal(board)
    if output == Move.X:
        print("X's won!")
    elif output == Move.O:
        print("0's won!")

    output = _check_vertical(board)
    if output == Move.X:
        print("X's won!")
    elif output == Move.O:
        print("0's won!")

    output = _check_horizontal(board)
    if output == Move.X:
        print("X's won!")
    elif output == Move.O:
        print("0's won!")

    print("Game ended with a draw!")


def print_board(board: List[List[Move]]):
    for row in board:
        for element in row:
            if element == Move.EMPTY:
                print("| - |", end="")
            elif element == Move.X:
                print("| X |", end="")
            else:
                print("| O |", end="")

        print()

    print("\n\n")


def _check_board_full(board) -> bool:
    for row in board:
        for element in row:
            if element == Move.EMPTY:
                return False

    return True


def _check_horizontal(board) -> Move:
    counter_x = 0
    counter_o = 0

    for row in board:
        for element in row:
            if element == Move.X:
                counter_x += 1
            elif element == Move.O:
                counter_o += 1

        if counter_x == 3:
            return Move.X
        else:
            counter_x = 0

        if counter_o == 3:
            return Move.O
        else:
            counter_o = 0

    return Move.EMPTY


def _check_vertical(board) -> Move:
    counter_x = 0
    counter_o = 0

    for i in range(len(board)):
        for j in range(board):

            if board[j][i] == Move.X:
                counter_x += 1

            elif board[j][i] == Move.O:
                counter_o += 1

        if counter_x == 3:
            return Move.X
        else:
            counter_x = 0

        if counter_o == 3:
            return Move.O
        else:
            counter_o = 0

    return Move.EMPTY


def _check_diagonal(board) -> Move:
    if board[0][0] == Move.X and board[1][1] == Move.X and board[2][2] == Move.X:
        return Move.X

    if board[0][0] == Move.O and board[1][1] == Move.O and board[2][2] == Move.O:
        return Move.O

    if board[0][2] == Move.X and board[1][1] == Move.X and board[2][0] == Move.X:
        return Move.X

    if board[0][2] == Move.O and board[1][1] == Move.O and board[2][0] == Move.O:
        return Move.O

    return Move.EMPTY
