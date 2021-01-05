import random
import math

AI = 'X'
PLAYER = 'O'

HEURISTIC_VALUES = {'O': -1, 'X': 1, '.': 0}

def adapt_board_to_algorithm(board):
    game_board = [
        ['1', '.', '.', '.'],
        ['2', '.', '.', '.'],
        ['3', '.', '.', '.'],
        [' ', '1', '2', '3']
    ]

    for i in range(len(board)):
        gb_index = 1
        for j in range(len(board[i])):
            game_board[i][gb_index] = board[i][j]
            gb_index += 1

    return game_board

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
    board = adapt_board_to_algorithm(board)

    possible_move = generate_all_possible_moves(board)
    score = - math.inf if is_maximizing else math.inf
    best_move = None

    for move in possible_move: 
        board[move[0]][move[1]] = AI if is_maximizing else PLAYER
        possible_best_move = min_max_tic_tac_toe(board, move, not is_maximizing, -math.inf, math.inf)
        board[move[0]][move[1]] = '.'

        if possible_best_move > score and is_maximizing:
            best_move, score = move, possible_best_move            
           
        elif possible_best_move < score and not is_maximizing:
            best_move, score = move, possible_best_move
    
    return best_move[0], best_move[1] - 1


