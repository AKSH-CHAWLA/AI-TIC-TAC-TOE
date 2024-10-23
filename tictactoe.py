"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turn = ""
    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count(X)
    for row in board:
        o_count += row.count(O)

    if x_count == o_count :
        turn =X
    elif x_count>o_count:
        turn = O
    else :
        raise  NotImplementedError

    return turn

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possible_moves.append((row,col))
    
    return possible_moves

def result(board, action ):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    row , col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy
        
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range (3):
        if board[row][0]==board[row][1]==board[row][2]!= "":
            return board[row][0]
    for col in range (3):
        if board[0][col]==board[1][col]==board[2][col]!= "":
            return board[0][col]
    if board[0][0] == board[1][1]==board[2][2]!="":   
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0]!="":
        return board[0][2]
    return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = 0
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                count+=1
    if count == 0 or winner(board)==X or winner(board)==O:
        return True
    elif winner(board)==None and count >=0:
        return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
def max_value(board) :
    v = -math.inf
    if terminal(board):
        return utility(board) 
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v
def min_value(board):
    v = math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    
    if current_player == X:
        best_value = -math.inf
        best_move = None
        for action in actions(board):
            move_value = min_value(result(board, action))  
            if move_value > best_value:
                best_value = move_value
                best_move = action
        return best_move
    else:
        best_value = math.inf
        best_move = None
        for action in actions(board):
            move_value = max_value(result(board, action))  
            if move_value < best_value:
                best_value = move_value
                best_move = action
        return best_move

