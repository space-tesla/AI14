# Q.2 Write a Python program to simulate the n-Queens problem.

# Function to check if a queen can be placed at board[row][col]
def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    
    return True

# Function to solve n-Queens problem using backtracking
def solve_n_queens(board, row, n):
    # If all queens are placed
    if row >= n:
        return True

    # Try placing this queen in all columns one by one
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            if solve_n_queens(board, row + 1, n):  # Recur to place next queen
                return True
            board[row][col] = 0  # Backtrack if placement does not lead to solution
    
    return False

# Function to print the board
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] == 1 else '.', end=' ')
        print()

# Main function to solve the n-Queens problem
def n_queens(n):
    # Initialize the chessboard with 0's
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    if solve_n_queens(board, 0, n):
        print_board(board, n)
    else:
        print("Solution does not exist.")

# Input: Number of queens
n = int(input("Enter the number of queens: "))
n_queens(n)



Output:
Enter the number of queens: 4
Q . . .
. . . Q
. Q . .
. . Q .