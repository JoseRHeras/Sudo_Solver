
from tictactoe import PLAYER
import math

def generate_all_possible_states(board):
    pass

def is_terminal(board):

    for i in range(len(board) - 1):
        row = board[i]
        for j in range (1, len(row)):
            if row[j] == '.':
                return False

    return True

def heuristic_evaluation(board, player, is_maximazing):
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

    ##Is a full table
    are_there_more_options = False
    for i in range(len(board) - 1):
        row = board[i]
        for j in range (1, len(row)):
            if row[j] == '.':
                are_there_more_options = True

    if are_there_more_options:
        return None

    return 0

def min_max_tic_tac_toe(board, player, maximize):
    if score := heuristic_evaluation(board, player, maximize) != None:
        return score

    if maximize:
        enemy_player = 'X' if player == 'X' else 'O'
        possible_states = generate_all_possible_states(board)
        max_score = - math.inf
        
        for state in possible_states:
            max_score = max(min_max_tic_tac_toe(state, enemy_player, False), max_score)
            
    else:


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
    ['1', 'X', 'O', 'X'],
    ['2', 'O', '.', 'X'],
    ['3', 'X', 'X', 'O'],
    [' ', '1', '2', '3'],
]

# print(is_terminal(table))
# print(is_terminal(table2))
# print(is_terminal(table3))
# print(heuristic_evaluation(table4, 'X', True))
print(-1 == None)
