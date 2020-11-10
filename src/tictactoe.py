import sys
import random
import os
import re

from minimax import heuristic_evaluation


AI = None
PLAYER = None
is_ai_first = True
available_commands = ('1', '2', '3', 'f', 's', 'r', 'help')
symbol_values = {'O': -1, 'X': 1, '.': 0}

def display_game_board_on_cmd(game_board):
    for row in game_board:
        print(row)

def update_game_board_with(row, col, game_board, player_symbol):
    game_board[row][col] = player_symbol

def get_valid_user_input(game_board):

    while True:   
        try:
            row = input('Enter the row: ')
            if not (re.match('[1-3]', row)):
                raise ValueError('The row input is not valid')

            if len(row) > 1:
                raise ValueError('The row value is not valid')

            col = input('Enter the col: ')
            if not (re.match('[1-3]', col)):
                raise ValueError('The col input is not valid')

            if len(col) > 1:
                raise ValueError('The col value is not valid')

            row = int(row) - 1
            col = int(col)

            if game_board[row][col] != '.':
                raise ValueError('Position already occupied.')
                
            break
        except ValueError as err:
            print(err)

        
    return row, col


# def get_heuristic_evaluation(board, move):
    global symbol_values

    score = 0
    ##Evaluate horizontal winning
    for i in range(1, len(board)):
        symbol = board[move[0]][i]
        score += symbol_values[symbol]

    if abs(score) == 3:
        return 1 if score > 0 else -1


    ##Evaluate vertical
    score = 0
    for i in range(len(board) - 1):
        key = board[i][move[1]]
        score += symbol_values[key]
        
    if abs(score) == 3:
        return 1 if score > 0 else -1

    ##Cross evaluation top to button
    score = 0
    for i in range(len(board) - 1):
        key = board[i][i + 1]
        score += symbol_values[key]

    if abs(score) == 3:
        return 1 if score > 0 else -1

    ##Cross evaluation button up
    score = 0
    for i in range(len(board) - 1):
        key = board[i][len(board) - 1 - i]
        score += symbol_values[key]
        
    if abs(score) == 3:
        return 1 if score > 0 else -1

    ##Evaluate lef spaces return 0 if there are any
    for row in range(len(board) - 1):
        for col in range(1, len(board)):
            if board[row][col] == '.':
                return 0
    
    ##Return None if the game is a tie 
    return None

def get_heuristic_evaluation(board, move):
    global symbol_values

    score = 0
    ##Evaluate horizontal winning
    for i in range(1, len(board)):
        symbol = board[move[0]][i]
        score += symbol_values[symbol]

    if abs(score) == 3:
        return 1 if score > 0 else -1


    ##Evaluate vertical
    score = 0
    for i in range(len(board) - 1):
        key = board[i][move[1]]
        score += symbol_values[key]
        
    if abs(score) == 3:
        return 1 if score > 0 else -1

    ##Cross evaluation top to button
    score = 0
    for i in range(len(board) - 1):
        key = board[i][i + 1]
        score += symbol_values[key]

    if abs(score) == 3:
        return 1 if score > 0 else -1

    ##Cross evaluation button up
    score = 0
    for i in range(len(board) - 1):
        key = board[i][len(board) - 1 - i]
        score += symbol_values[key]
        
    if abs(score) == 3:
        return 1 if score > 0 else -1

    ##Evaluate lef spaces return 0 if there are any
    for row in range(len(board) - 1):
        for col in range(1, len(board)):
            if board[row][col] == '.':
                return 0
    
    ##Return None if the game is a tie 
    return None

    
def get_optimal_move(game_board):
    global AI


    for row in range(len(game_board) - 1):
        for col in range(1, len(game_board)):
            if game_board[row][col] == '.':
                return row, col
    
def execute_tictactoe():
    global AI
    global PLAYER

    is_game_over = False
    is_AI_Turn = is_ai_first
    heuristic_evaluation = None
    winner_player = None

    game_board = [
        ['1', '.', '.', '.'],
        ['2', '.', '.', '.'],
        ['3', '.', '.', '.'],
        [' ', '1', '2', '3']
    ]

    while not is_game_over:

        if is_AI_Turn:
            print("A.I. turn")
            
            ai_row, ai_col = get_optimal_move(game_board)
            update_game_board_with(ai_row, ai_col, game_board, AI)
            # is_game_over = get_state_of_game_from(game_board)
            heuristic_evaluation = get_heuristic_evaluation(game_board, [ai_row, ai_col])

            if heuristic_evaluation != None:
                winner_player = AI
                break
        
            print(f"AI chooses the following: {ai_row} {ai_col}")
            display_game_board_on_cmd(game_board)

            x = input("Hit enter to continue")
            os.system('cls')
            is_AI_Turn = False

        else:
            print('Your Turn')
            display_game_board_on_cmd(game_board)

            print('Make your move:\n')
            us_row, us_col = get_valid_user_input(game_board)
            update_game_board_with(us_row, us_col, game_board, PLAYER)
            heuristic_evaluation = get_heuristic_evaluation(game_board, [us_row, us_col])
            if heuristic_evaluation_ != None:
                winner_player = PLAYER
                break

            os.system('cls')
            print('You took your move!!')           
            display_game_board_on_cmd(game_board)

            x = input('Hit enter to continue')
            os.system('cls')
            is_AI_Turn = True

    if heuristic_evaluation == 0:
        print("The game is a draw")
    elif heuristic_evaluation == 1:
        print(f"Player {winner_player} wins")


def configure_game(configuration=None):
    global is_ai_first
    global AI
    global PLAYER

    if configuration == None:
        AI = 'O' if random.randint(0, 9) % 2 == 0 else 'X'
        PLAYER = 'X'if AI == 'O' else 'O'
        is_ai_first = True if AI == 'X' else False

    elif '1' in configuration:
        is_ai_first = False
        AI = 'O'
        PLAYER = 'X'
    elif '2' in configuration:
        is_ai_first = True
        AI = 'X'
        PLAYER = 'O'
          

def inputs_are_valid(user_input):
    for item in range(1, len(user_input)):
        if str(user_input[item]) not in available_commands:
            return False
    
    return True

def output_help_information():
    print("Welcome to tictactoe")
    print("Rules of the game: \n1. There are two players: 'X' and 'O' \n2. Player X always goes first \n3. Player that connects three dots in line first wins")
    print("3. A connected line could be diagonal, vertical or horizontal")
    print("\nHow to Play:")

    print("To choose where you want to put your next input enter the coordinates on the following format: row_number col_numbe \n")
    print("By default the game chooses the starting player randomly \nAlternative you can include the following commands:")

    print("'1' to start first")
    print("'2' to start second")

def main(user_input):

    if len(user_input) > 1:
        if('help' in user_input):
            output_help_information()
        else:
            if inputs_are_valid(user_input):
                configure_game(user_input)
                # print(f"{AI}, {PLAYER}, {is_ai_first}")
                execute_tictactoe()
            else:
                print("Non valid commands given. \nPlease use the 'help' command to view available commands")
    else:
        configure_game()
        # print(f"{AI}, {PLAYER}, {is_ai_first}")
        execute_tictactoe()

if __name__ == "__main__":
    main(sys.argv)
