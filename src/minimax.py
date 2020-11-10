
from tictactoe import PLAYER
import math

from tictactoe import *


symbol_values = {'O': -1, 'X': 1, '.': 0}



def generate_all_possible_moves(board):
    possible_moves = []

    for row in range(len(board) - 1):
        for col in range(1, len(board)):
            if board[row][col] == '.':
                possible_moves.append((row, col))
    
    return possible_moves

def min_max_tic_tac_toe(board, move, maximize):
    
    if score := get_heuristic_evaluation(board, move) != None:
        return score

    possible_moves = generate_all_possible_moves(board)

    if maximize:           
        max_score = - math.inf
        
        for move in possible_moves:
            board[move[0]][move[1]] = AI
            potential_score = min_max_tic_tac_toe(board, move, False)
            max_score = max(max_score, potential_score)
            board[move[0]][move[1]] = '.'

        return max_score
            
    else:
        min_score = math.inf
        
        for move in possible_moves:
            board[move[0]][move[1]] = PLAYER
            potential_score = min_max_tic_tac_toe(board, move, True)
            min_score = min(potential_score, min_score)
            board[move[0]][move[1]] = '.'

        return min_score

def get_best_move(board):
    possible_move = generate_all_possible_moves(board)
    score = - math.inf
    best_move = None

    for move in possible_move:
        board[move[0]][move[1]] = AI
        possible_best_move = min_max_tic_tac_toe(board, move, False)
        board[move[0]][move[1]] = '.'
        
        if possible_best_move > score:
            best_move = move
            score = possible_best_move

    return best_move[0], best_move[1]

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
    ['1', 'O', 'O', 'O'],
    ['2', 'X', 'O', 'X'],
    ['3', 'X', 'X', 'X'],
    [' ', '1', '2', '3'],
]
move = [2, 1]
player = 'X'

