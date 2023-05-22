from random import Random

from studentA import Move, is_game_over

import signal

random = Random()


def ai_move(board):
    available_moves = []

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == Move.EMPTY:
                available_moves.append((i, j))

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == Move.EMPTY:
                board[i][j] = Move.X
                if is_game_over(board):
                    board[i][j] = Move.O
                    return board
                else:
                    board[i][j] = Move.EMPTY

    move = random.choice(available_moves)
    board[move[0]][move[1]] = Move.O
    return board


def get_user_move(board):
    available_moves = []

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == Move.EMPTY:
                available_moves.append((i, j))

    while True:
        print("Enter your move:")
        print("After 5 seconds, the AI will make a move.")

        def handler(signum, frame):
            raise Exception("timeout")
        
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(5)

        try:
            x = int(input("Row: "))
            y = int(input("Column: "))
            signal.alarm(0)
        except Exception as e:
            print("You took too long to make a move. AI will make a move.")
            move = random.choice(available_moves)
            x = move[0]
            y = move[1]
            print("AI chose row {} and column {}".format(x, y))
            board[x][y] = Move.X
            continue

        signal.alarm(0)

        if (x, y) in available_moves:
            board[x][y] = Move.X
            return board
        else:
            print("Invalid move. Try again.")


def is_player_starting():
    print("Head or tails? (h/t)")
    choice = input()
    return random.choice(["h", "t"]) == choice
