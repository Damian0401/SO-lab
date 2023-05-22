
from random import Random

random = Random()

def ai_move(board):
    pass

def get_user_move(board):
    pass

def is_player_starting():
    print("Head or tails? (h/t)")
    choice = input()
    return random.choice(["h", "t"]) == choice