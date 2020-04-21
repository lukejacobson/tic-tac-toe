from copy import deepcopy

PLAYER_1 = 'X'
COMPUTER = 'O' 

# called when its COMPUTER's move
def getNextMove(board, player):
    # get all posible moves:
    move_value = {}
    for i,row in enumerate(board):
        for j,tile in enumerate(row):
            if tile == ' ':
                move_value[(i,j)] = 0
    
    # find minimax values for each move
    for key in move_value:
        move_value[key] = minimax_value(key,board,COMPUTER)

    reccomended_move = max([(val,key) for (key,val) in move_value.items()])[1]
    return reccomended_move

# finds minimax value for the given move on the given board
def minimax_value(move,board,player):
    temp_board = deepcopy(board)

    # apply move to board, and do terminal test
    temp_board[move[0]][move[1]] = player
    #print_board(temp_board)
    utility = isEndState(temp_board)
    #print("Utility", utility)
    #print("Utility Bool", isInt(utility))
    #print("Utility", utility)
    if not (utility is False):
        return utility
    #print("Utility", utility)
    # now we expand game states
    possible_move_vals = {}
    for i,row in enumerate(temp_board):
        for j,tile in enumerate(row):
            if tile == ' ':
                possible_move_vals[(i,j)] = minimax_value(
                    (i,j), temp_board, next_player(player))
    
    if player == COMPUTER:
        return max([(val,key) for (key,val) in possible_move_vals.items()])[0]
    else:
        return min([(val,key) for (key,val) in possible_move_vals.items()])[0]


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
