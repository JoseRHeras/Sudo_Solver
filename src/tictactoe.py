import sys
import random
import os
import re

AI = None
PLAYER = None
is_ai_first = True
available_commands = ('1', '2', '3', 'f', 's', 'r', 'help')

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

            col = input('Enter the col: ')
            if not (re.match('[1-3]', col)):
                raise ValueError('The col input is not valid')

            row = int(row) - 1
            col = int(col)

            if game_board[row][col] != '.':
                raise ValueError('Position already occupied.')
                
            break
        except ValueError as err:
            print(err)

        
    return row, col

def get_state_of_game_from(game_board):
    pass
    
def execute_tictactoe():

    is_game_over = False
    game_board = [
        ['1', '.', '.', '.'],
        ['2', '.', '.', '.'],
        ['3', '.', '.', '.'],
        [' ', '1', '2', '3']
    ]

    is_AI_Turn = True

    if is_ai_first:
        ai_row, ai_col = random.randint(0, 2), random.randint(1, 3)
        update_game_board_with(ai_row, ai_col, game_board, AI)
        is_AI_Turn = False

        print('AI first move:')
        display_game_board_on_cmd(game_board)

    while not is_game_over:

        if is_AI_Turn:
            print ('The board:')
            display_game_board_on_cmd(game_board)
            print ("\nAI is thinking:")
            ai_row, ai_col = get_ai_moves(game_board, AI)
            update_game_board_with(ai_row, ai_col, game_board, AI)
            is_game_over = get_state_of_game_from(game_board)

            os.system('cls')
            print("AI chooses the following:")
            display_game_board_on_cmd(game_board)
            is_AI_Turn = False

        else:
            if not is_AI_Turn: 
                os.system('cls')
                print('The board:')
                
            display_game_board_on_cmd(game_board)

            print('Make your move:\n')
            us_row, us_col = get_valid_user_input(game_board)
            update_game_board_with(us_row, us_col, game_board, PLAYER)
            is_game_over = get_state_of_game_from(game_board)

            os.system('cls')
            print('You took your move!!')
            is_AI_Turn = True
        
        print('The current game state is: ')

        x = input('slsx')
        os.system('cls')

def configure_game(configuration=None):
    global AI
    global PLAYER
    global is_ai_first

    if configuration == None:
        AI = 'X' if random.randint(1, 2) == 1 else 'O'
        PLAYER = 'O' if AI == 'X' else 'X'
        is_ai_first = True if random.randint(0, 10) % 2 == 0 else False
    else:
        if '3' in configuration:
            AI = 'X' if random.randint(1, 2) == 1 else 'O'
            PLAYER = 'O' if AI == 'X' else 'X'
        elif '2' in configuration:
            AI = 'X'
            PLAYER = 'O'
        elif '1' in configuration:
            AI = 'O'
            PLAYER = 'X'

        if 'r' in configuration:
            is_ai_first = True if random.randint(0, 10) % 2 == 0 else False
        elif 's' in configuration:
            is_ai_first = True
        elif 'f' in configuration:
            is_ai_first = False

def inputs_are_valid(user_input):
    for item in range(1, len(user_input)):
        if str(user_input[item]) not in available_commands:
            return False
    
    return True

def output_help_information():
    print("Welcome to tictactoe")
    print("To choose a row use the following format: row_number col_numbe \n")
    print("To play just execute the program as you will with any other python program \nAlternative you can include the following commands:")

    print("'1' to choose player 'X'")
    print("'2' to choose player 'O'")
    print("'3' to choose randomly \n")

    print("Further customization can be achieved with the following:")
    print("'f' to start first")
    print("'s' to start second")
    print("'r' to make it random")

def main(user_input):

    if len(user_input) > 1:
        if('help' in user_input):
            output_help_information()
        else:
            if inputs_are_valid(user_input):
                configure_game(user_input)
                execute_tictactoe()
            else:
                print("Non valid commands given. \nPlease use the 'help' command to view available commands")
    else:
        configure_game()
        execute_tictactoe()

if __name__ == "__main__":
    main(sys.argv)
