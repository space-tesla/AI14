# Q.2 Write a Python program to simulate the n-Queens problem.

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, row, n):
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  
            if solve_n_queens(board, row + 1, n):  
                return True
            board[row][col] = 0  
    
    return False
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] == 1 else '.', end=' ')
        print()

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    if solve_n_queens(board, 0, n):
        print_board(board, n)
    else:
        print("Solution does not exist.")

n = int(input("Enter the number of queens: "))
n_queens(n)



"""Output:
Enter the number of queens: 4
Q . . .
. . . Q
. Q . .
. . Q ."""