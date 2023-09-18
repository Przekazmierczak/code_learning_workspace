"""
Tic Tac Toe Player
"""

import math

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
    turns = 0
    for i in range(3):
        for row_element in board[i]:
            if row_element == X or row_element == O:
                turns += 1
    if turns % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for i in range(3):
        for j in range(3):
            row_element = board[i][j]
            if row_element == EMPTY:
                move = (i, j)
                moves.append(move)
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    i, j = action
    if board_copy[i][j] == EMPTY:   
        board_copy[i][j] = player(board)
    else:
        raise ValueError("Invalid action")
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def winner(board):
        winning_states = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
        for winning_state in winning_states:
            winner_list = []
            for position in winning_state:
                i, j = position
                winner = board[i][j]
                winner_list.append(winner)
            if winner_list == [X, X, X]:
                return X
            if winner_list == [O, O, O]:
                return O
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for row in board:
        for element in row:
            if element == EMPTY:
                return False
    return True


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_values(state):
        v = float('-inf')
        if terminal(state):
            return utility(state)
        for action in actions(state):
            v = max(v, min_values(result(state, action)))
            return v

    def min_values(state):
        v = float('inf')
        if terminal(state):
            return utility(state)
        for action in actions(state):
            v = min(v, max_values(result(state, action)))
            return v

    current_player = player(board)
    possible_actions = actions(board)
    actions_list = []
    for possible_action in possible_actions:
        if current_player == X:
            v = min_values(result(board, possible_action))
        else:
            v = max_values(result(board, possible_action))
        actions_list.append([v, possible_action])
    if current_player == X:
        actions_list.sort(key=lambda x: x[0], reverse=True)
    else:
        actions_list.sort(key=lambda x: x[0])
    return actions_list[0][1]