

def ScanDanger(n,board , row , col):
    """Can the board for attacking queens

    Args:
        n (int): board size
        board (list): chessboard
        row (int): row of the given queen
        col (int): column of the given queen
    
    Returns:
        boolean: false if safe, true if not
    """
    
    # top-left direction
    i = row
    j = col
    while(i>=0 and j>=0):
        if(board[i][j] == "Q"):
            return True
        if(board[i][j] == "W"):
            break
        i-= 1
        j-= 1
    
    #top-right
    while(i>= 0 and j < n):
        if(board[i][j] == "Q"):
            return True
        if(board[i][j]== "W"):
            break
        i-= 1
        j+= 1   
    
    # top
    while(i>=0):
        if(board[i][j] == "Q"):
            return True
        if(board[i][j]== "W"):
            break
        i-= 1
        
    return False


def placeQinRow(board, n , row):
    pass


def placeQ(board, n, row , W1 , W2):
    pass