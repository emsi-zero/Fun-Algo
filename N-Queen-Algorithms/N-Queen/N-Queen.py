

solutions =[]           # All possible solutions of N Queen Problem
n = None                   # Dimesion of the board
board = None           # n*n Board


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
    """queen placement recursicve function that places the queens based on privously placed queens and finds a solution

    Args:
        row (int): row number of the queen

    Returns:
        boolean: whether there is a solution or not
    """
    
    # base case
    # If all queens are placed safely return true and save the solution
    if row == n:
        solution = []
        for i in range(0,n):
            for j in range(0,n):
                if board[i][j] == "Q":
                    solution.append((i,j))
        solutions.append(solution)
        return True
    
    col = 0
    
    while col < n:
        if not(ScanDanger(row , col)):
            board[row][col] = "Q"
            PlaceQ(row + 1)
            board[row][col] = " "
        
        col+=1

def printBoard():
    for i in range(0,n):
            print(board[i])

def clearBoard():
    board = [[" " for i in range(0,n)] for j in range(0,n)]
    

def printSolutions():
    for s in solutions:
        for q in s:
            board[q[0]][q[1]] = "Q"
        printBoard()
        clearBoard()

def printSolution(x):
    for q in solutions[x]:
        board[q[0]][q[1]] = "Q"
    printBoard()
    clearBoard()

n = 8
board = [[" " for i in range(0,n)] for j in range(0,n)]
PlaceQ(0)
print(len(solutions))