

solutions =[]           # All possible solutions of N Queen Problem
n = 0                   # Dimesion of the board
board = [[" " * n] *n]            # n*n Board


def ScanDanger(row ,col):
    """Checks for dangers of attacking queens 

    Args:
        row (int): row number
        col (int): col number

    Returns:
        boolean: danger of attacking queens
    """
    # top-left direction
    i = row
    j = col
    while(i>=0 and j>=0):
        if board[i][j] == "Q":
            return True
        i-= 1
        j-= 1
    
    # top direction
    i = row
    while(i>=0):
        if board[i][col] == "Q":
            return True
        i-=1
    
    # top-right direction
    i = row
    j = col
    while( i>=0 and j<n):
        if board[i][j] == "Q":
            return True
        i-=1
        j+=1
    
    return False

def PlaceQ(row):
    
    # base case
    # If all queens are placed safely return true and save the solution
    if row == n:
        solution = []
        for i in board:
            for j in board[i]:
                if board[i][j] == "Q":
                    solution.append((i,j))
        solutions.append(solution)
        return True
    

def printBoard():
    pass

def clearBoard():
    pass

def printSolutions():
    pass

