from copy import deepcopy

PLAYER_1 = 'X'
COMPUTER = 'O' 

INF = 2147483647

# called when its COMPUTER's move
def getNextMove(board, player):
    # parameters for pruning
    alpha = -INF
    beta = INF
    # get all posible moves:
    move_value = {}
    for i,row in enumerate(board):
        for j,tile in enumerate(row):
            if tile == ' ':
                move_value[(i,j)] = 0
    
    # find minimax values for each move
    for key in move_value:
        move_value[key] = minimax_value(key,board,COMPUTER,alpha,beta)
    
    print("MINIMAX: ", move_value)

    reccomended_move = max([(val,key) for (key,val) in move_value.items()])[1]
    return reccomended_move

# finds minimax value for the given move on the given board
def minimax_value(move,board,player,alpha,beta):
    temp_board = deepcopy(board)

    # NOTE: player is the player who made the move to get to THIS board state.

    # apply move to board, and do terminal test
    temp_board[move[0]][move[1]] = player
    utility = isEndState(temp_board)
    
    if not (utility is False):
        return utility

    if player == COMPUTER:
        # this is a MIN node, 
        value = INF
        for i,row in enumerate(temp_board):
            for j,tile in enumerate(row):
                if tile == ' ':
                    value = min(value, minimax_value(
                        (i,j), temp_board, next_player(player), alpha, beta))
                    if value <= alpha:
                        return value
                    beta = min(value, beta)
        return value
    
    else:
        # this is a MAX node, 
        value = -INF
        for i,row in enumerate(temp_board):
            for j,tile in enumerate(row):
                if tile == ' ':
                    value = max(value, minimax_value(
                        (i,j), temp_board, next_player(player), alpha, beta))
                    if value >= beta:
                        return value
                    alpha = max(value, alpha)
        return value
        
        

    # # now we expand game states
    # possible_move_vals = {}
    # for i,row in enumerate(temp_board):
    #     for j,tile in enumerate(row):
    #         if tile == ' ':
    #             v = minimax_value(
    #                 (i,j), temp_board, next_player(player), alpha, beta)
    #             possible_move_vals[(i,j)] = 
    
    # if player == COMPUTER:

    #     return min([val for (key,val) in possible_move_vals.items()])
    # else:
    #     return max([val for (key,val) in possible_move_vals.items()])


def next_player(player):
    if player == COMPUTER:
        return PLAYER_1
    return COMPUTER

def isEndState(board):
    win = isWinState(board)
    draw = isDrawState(board)
    if win == COMPUTER:
        return 1
    elif win == PLAYER_1:
        return -1
    elif draw:
        return 0
    return False
    

def isWinState(board):

    for row in board:
        if row[0] != ' ' and len(list(set(row))) == 1:
            return row[0]
    
    for i in range(3):
        col = [row[i] for row in board]
        if col[0] != ' ' and len(list(set(col))) == 1:
            return col[0]
    
    diag = [board[i][i] for i in range(3)]
    if diag[0] != ' ' and len(list(set(diag))) == 1:
        return diag[0]

    diag = [board[i][2-i] for i in range(3)]
    if diag[0] != ' ' and len(list(set(diag))) == 1:
        return diag[0]
    
    return False

def isDrawState(board):
    for row in board:
        for tile in row:
            if tile == ' ':
                return False
    return True

def isInt(i):
    try:
        int(i)
        return True
    except:
        return False

def print_board(board):
    print("\n\n######################")
    print("Board:")
    for row in board:
        print(row)
    print("######################")

if __name__ == '__main__':
    board = [
        ['X','O','O'],
        ['X',' ',' '],
        ['O',' ',' '],
    ]
    player = 'X'
    print(getNextMove(board, player))
