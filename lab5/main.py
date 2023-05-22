from studentA import print_board, is_game_over, new_board
from studentB import ai_move, get_user_move, is_player_starting

board = new_board(3)
user_turn = is_player_starting()

while not is_game_over(board):
    print_board(board)
    board = get_user_move(board) if user_turn else ai_move(board)
    user_turn = not user_turn
