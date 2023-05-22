from enum import Enum
from typing import List


class Move(Enum):
    X = 1
    Y = 2
    EMPTY = 0


def new_board(size=3):
    board = []
    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(Move.EMPTY)

        board.append(row)

    return board


def is_game_over(board: List[List[Move]]) -> bool:
    for row in board:
        for element in row:
            if element == Move.EMPTY:
                return False


def print_board(board: List[List[Move]]):
    for row in board:
        for element in row:
            if element == Move.EMPTY:
                print("0")
            elif element == Move.X:
                print("X")
            else:
                print("Y")