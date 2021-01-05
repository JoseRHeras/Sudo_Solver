import sys
import random
import os
import re
import math
import platform


AI = 'X'
PLAYER = 'O'
IS_AI_FIRST = True
AI_MODE = False
COMMANDS = ('1', '2', 'A', 'help')
HEURISTIC_VALUES = {'O': -1, 'X': 1, '.': 0}
CLEAR_COMMAND = 'cls' if platform.system() == 'Windows' else 'clear'

def display_game_board_on_cmd(game_board):
    for row in game_board:
        print(row)

def update_game_board_with(row, col, game_board, player_symbol):
    game_board[row][col] = player_symbol

def update_screen_with(game_board, row, col, player=None):
    if AI_MODE or player != None:
        print(f"{player} chooses the following: {row + 1} {col}")
    else:
        print('Move made!!\n') 

    display_game_board_on_cmd(game_board)
    input("\nHit enter to continue")
    os.system('cls')

def get_valid_user_input(game_board):
    while True:   
        try:
            user_coordinates = input("Enter your choice 'row, col': ")
            user_coordinates =[ x for x in user_coordinates.replace(" ", "")]
            
            if len(user_coordinates) == 2:
                for location in user_coordinates:
                    if re.match('[^1-3]', location):
                        raise ValueError('Input given is not valid')

                row, col = int(user_coordinates[0]) - 1, int(user_coordinates[1])
                if game_board[row][col] != '.':
                    raise ValueError('Position already occupied.')               
            else:
                raise ValueError('Input given is not valid')

            return row, col
        except ValueError as error:
            print(error)


def get_heuristic_evaluation(board, move):
    
    score = 0
    ##Horizontal evaluation
    for i in range(1, len(board)):
        symbol = board[move[0]][i]
        score += HEURISTIC_VALUES[symbol]

    if abs(score) == 3:
        return 1 if score > 0 else -1

    ##Vertical evaluation
    score = 0
    for i in range(len(board) - 1):
        key = board[i][move[1]]
        score += HEURISTIC_VALUES[key]
        
    if abs(score) == 3:
        return 1 if score > 0 else -1

    ##Cross evaluation top to button
    score = 0
    for i in range(len(board) - 1):
        key = board[i][i + 1]
        score += HEURISTIC_VALUES[key]

    if abs(score) == 3:
        return 1 if score > 0 else -1

    ##Cross evaluation button up
    score = 0
    for i in range(len(board) - 1):
        key = board[i][len(board) - 1 - i]
        score += HEURISTIC_VALUES[key]
        
    if abs(score) == 3:
        return 1 if score > 0 else -1

    ##Evaluates for non-used spaces. Returns None if spaces left
    for row in range(len(board) - 1):
        for col in range(1, len(board)):
            if board[row][col] == '.':
                return None
    
    ##Return 0 if the game is a tie 
    return 0


def generate_all_possible_moves(board):
    possible_moves = []

    for row in range(len(board) - 1):
        for col in range(1, len(board)):
            if board[row][col] == '.':
                possible_moves.append([row, col])
    

    if len(possible_moves) > 5:
        random.shuffle(possible_moves)

    return possible_moves

def min_max_tic_tac_toe(board, move, maximize, alpha, beta):    
    score = get_heuristic_evaluation(board, move)
    if score != None:
        return score

    possible_moves = generate_all_possible_moves(board)

    if maximize:           
        max_score = - math.inf
        
        for move in possible_moves:
            board[move[0]][move[1]] = AI
            potential_score = min_max_tic_tac_toe(board, move, False, alpha, beta)
            max_score = max(max_score, potential_score)
            board[move[0]][move[1]] = '.'

            alpha = max(alpha, max_score)
            if beta <= alpha:
                break

        return max_score
            
    else:
        min_score = math.inf
        
        for move in possible_moves:
            board[move[0]][move[1]] = PLAYER
            potential_score = min_max_tic_tac_toe(board, move, True, alpha, beta)
            min_score = min(potential_score, min_score)
            board[move[0]][move[1]] = '.'

            beta = min(beta, min_score)
            if beta <= alpha:
                break

        return min_score

def get_best_move(board, is_maximizing=True):
    print(is_maximizing)
    possible_move = generate_all_possible_moves(board)
    score = - math.inf if is_maximizing else math.inf
    best_move = None

    for move in possible_move: 
        board[move[0]][move[1]] = AI if is_maximizing else PLAYER
        possible_best_move = min_max_tic_tac_toe(board, move, not is_maximizing, -math.inf, math.inf)
        board[move[0]][move[1]] = '.'

        if possible_best_move > score and is_maximizing:
            print(possible_best_move)
            print(move)
            best_move, score = move, possible_best_move            
           
        elif possible_best_move < score and not is_maximizing:
            best_move, score = move, possible_best_move
    
    return best_move[0], best_move[1]


def ai_makes_move_and_get_result(player_icon, game_board, ai_turn):
    player_name = 'Kike A.I.' if player_icon == 'X' else 'Kuru A.I.'
    print(f"{player_name} turn")
            
    ai_row, ai_col = get_best_move(game_board, ai_turn)
    update_game_board_with(ai_row, ai_col, game_board, player_icon)

    game_state = get_heuristic_evaluation(game_board, [ai_row, ai_col])
            
    if game_state == None:             
        update_screen_with(game_board, ai_row, ai_col, player_name)
        return not ai_turn, game_state
    
    return None, game_state

def execute_tictactoe():
    
    is_AI_Turn = IS_AI_FIRST
    state_of_the_game = None

    game_board = [
        ['1', '.', '.', '.'],
        ['2', '.', '.', '.'],
        ['3', '.', '.', '.'],
        [' ', '1', '2', '3']
    ]

    while True:
        
        os.system(CLEAR_COMMAND)
        if is_AI_Turn:
            is_AI_Turn, state_of_the_game = ai_makes_move_and_get_result(AI, game_board, is_AI_Turn)
            if is_AI_Turn == None:
                break
        else:
            if AI_MODE:
                is_AI_Turn, state_of_the_game = ai_makes_move_and_get_result(PLAYER, game_board, is_AI_Turn)               
                if is_AI_Turn == None:
                    break
            else:
                print('Your Turn\n')
                display_game_board_on_cmd(game_board)

                print('\nMake your move:\n')
                us_row, us_col = get_valid_user_input(game_board)
                update_game_board_with(us_row, us_col, game_board, PLAYER)
                state_of_the_game = get_heuristic_evaluation(game_board, [us_row, us_col])
               
                if state_of_the_game == None:              
                    os.system(CLEAR_COMMAND)
                    update_screen_with(game_board, us_row, us_col)
                    is_AI_Turn = True
                else:
                    break
    
    os.system(CLEAR_COMMAND)
    print("The verdict\n")
    display_game_board_on_cmd(game_board)

    if state_of_the_game == 0:
        print("\nThe game is a draw")
    elif state_of_the_game == 1:
        print(f"\nKike A.I. Wins")
    else:
        print ("\nKuru A.I. wins") if AI_MODE else ("\nYou Win")

def configure_game(configuration=None):
    global IS_AI_FIRST
    global AI_MODE

    if configuration == None or 'A' in configuration:     
        IS_AI_FIRST = True if random.randint(0, 9) % 2 == 0 else False
        
        if configuration != None:
            AI_MODE = True
    else:
        IS_AI_FIRST = False if '1' in configuration else True

        
def inputs_are_valid(user_input):
    for item in range(1, len(user_input)):
        if str(user_input[item]) not in COMMANDS:
            return False
    
    return True

def printout_help_information_to_screen():
    print("\nWelcome to Tic-Tac-Toe\n")
    print("Rules of the game: \n1. There are two players: 'X' and 'O' \n2. AI uses 'X' \n3. Human player uses 'O' ")
    print("4. Player that connects three dots in line first wins")
    print("5. A connected line could be diagonal, vertical or horizontal")
    print("\nHow to Play:")

    print("-To choose where you want to put your next input enter the coordinates on the following format: row_number col_number")
    print("-After each move the game will wait until you hit \"Enter\" to contine to the next step")
    print("-By default the game starts as Player vs A.I. game where first player is chosen randomly\n")
    print("-Alternative you can include the following commands using the format \"py.exe tictactoe.py #comand#\"\n")
    print("Commands available:")
    print("'1' to start first")
    print("'2' to start second")
    print("'A' to let Kike A.I. and Kuru A.I. do a machine vs machine demonstration\n")

    print("P.S. Kuru and Kike are the names I have chosen for the A.I. in this game.(No special meaning behind)\n")

def main(user_input):

    if len(user_input) > 1:
        if('help' in user_input):
            printout_help_information_to_screen()
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

