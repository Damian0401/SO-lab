
from random import Random

from studentA import Move

random = Random()

def ai_move(board):
    available_moves = []

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == Move.EMPTY:
                available_moves.append((i, j))

    return random.choice(available_moves)

def get_user_move(board):
    available_moves = []

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == Move.EMPTY:
                available_moves.append((i, j))
    
    while True:
        print("Enter your move:")
        print("x: ")
        x = int(input())
        print("y: ")
        y = int(input())

        if (x, y) in available_moves:
            board[x][y] = Move.X
            return board
        else:
            print("Invalid move. Try again.")
    

def is_player_starting():
    print("Head or tails? (h/t)")
    choice = input()
    return random.choice(["h", "t"]) == choice