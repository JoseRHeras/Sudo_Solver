
from tictactoe import PLAYER
import math


symbol_values = {'O': -1, 'X': 1, '.': 0}


def generate_all_possible_states(board):
    pass

def heuristic_evaluation(board, player, is_maximazing):
    #Returns 1 in terminal state with a maximizing score
    #Returns -1 in terminal state wiht a  minimizing score
    #Returns None if game not in terminal state
    #Returns 0 if game in terminal state but not winner

    ##Horizontal Evaluation
    for i in range(len(board) - 1):
        row = board[i]
        winning_row = True
        for j in range(1, len(row)):
            if row[j] != player:
                winning_row = False

        if(winning_row):
            print("horizontal")
            return 1 if is_maximazing else -1


    ##Vertical Evaluation
    for i in range(1, len(board)):
        winning_row = True
        for j in range(len(board) - 1):
            if board[j][i] != player:
                winning_row = False
                break

        if(winning_row):
            print('vertical')
            return 1 if is_maximazing else -1

    ##Cross evaluation top to button
    winning = True
    for i in range(len(board) - 1):
        winning = True
        if board[i][i + 1] != player:
            winning = False
            break

    if winning:
        print('cross1')
        return 1 if is_maximazing else -1

    ##Cross evaluation button up
    winning = True
    for i in range(len(board) - 1):
        if board[i][len(board) - 1 - i] != player:
            winning = False
            break

    if winning:
        print('cross2')
        return 1 if is_maximazing else -1

    ##Game Board has more options. Therefore not a terminal state
    are_there_more_options = False
    for i in range(len(board) - 1):
        row = board[i]
        for j in range (1, len(row)):
            if row[j] == '.':
                are_there_more_options = True

    if are_there_more_options:
        return None

    return 0


def generate_all_possible_moves(board):
    possible_moves = []

    for row in range(len(board) - 1):
        for col in range(1, len(board)):
            if board[row][col] == '.':
                possible_moves.append((row, col))
    
    return possible_moves

def min_max_tic_tac_toe(board, player, maximize):
    

    if score := heuristic_evaluation(board, player, maximize) != None:
        return score

    enemy_player = 'O' if player == 'X' else 'X'
    possible_moves = generate_all_possible_moves(board)

    if maximize:           
        max_score = - math.inf
        
        for move in possible_moves:
            board[move[0]][move[1]] = player
            potential_score = min_max_tic_tac_toe(board, enemy_player, False)
            max_score = max(max_score, potential_score)
            board[move[0]][move[1]] = '.'

        return max_score
            
    else:
        min_score = math.inf
        
        for move in possible_moves:
            board[move[0]][move[1]] = player
            potential_score = min_max_tic_tac_toe(board, enemy_player, True)
            min_score = min(potential_score, min_score)
            board[move[0]][move[1]] = '.'

        return min_score

def get_best_move(board, player):
    possible_move = generate_all_possible_moves(board)
    score = - math.inf
    best_move = None

    for move in possible_move:
        board[move[0]][move[1]] = player
        possible_best_move = min_max_tic_tac_toe(board, player, False)
        board[move[0]][move[1]] = '.'
        
        if possible_best_move > score:
            best_move = move
            score = possible_best_move

    return best_move

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


table =[
    ['1', 'O', '.', '.'],
    ['2', '.', '.', '.'],
    ['3', '.', '.', 'X'],
    [' ', '1', '2', '3'],
]

table2 =[
    ['1', 'O', 'c', 'c'],
    ['2', 'c', 'c', 'c'],
    ['3', 'c', 'c', 'X'],
    [' ', '1', '2', '3'],
]

table3 =[
    ['1', 'O', '.', 'c'],
    ['2', 'c', 'c', 'c'],
    ['3', 'c', 'c', 'X'],
    [' ', '1', '2', '3'],
]

table4 = [
    ['1', 'O', 'X', 'O'],
    ['2', 'X', 'O', 'X'],
    ['3', 'X', 'X', 'X'],
    [' ', '1', '2', '3'],
]
move = [2, 1]
player = 'X'
print(get_heuristic_evaluation(table4, move))
# print(is_terminal(table))
# print(is_terminal(table2))
# print(is_terminal(table3))
# print(heuristic_evaluation(table4, 'X', True))
# print(-1 == None)
# print(generate_all_possible_moves(table4))
