
from tictactoe import PLAYER
import math

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
    possible_states = generate_all_possible_states(board, player)

    if maximize:           
        max_score = - math.inf
        
        for state in possible_states:
            potential_score = min_max_tic_tac_toe(state, enemy_player, False)
            max_score = max(max_score, potential_score)

        return max_score
            
    else:
        min_score = math.inf
        
        for state in possible_states:
            potential_score = min_max_tic_tac_toe(state, enemy_player, True)
            min_score = min(potential_score, min_score)

        return min_score

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
    ['1', '.', '.', '.'],
    ['2', '.', '.', '.'],
    ['3', '.', '.', '.'],
    [' ', '1', '2', '3'],
]

# print(is_terminal(table))
# print(is_terminal(table2))
# print(is_terminal(table3))
# print(heuristic_evaluation(table4, 'X', True))
# print(-1 == None)
print(generate_all_possible_moves(table4))
