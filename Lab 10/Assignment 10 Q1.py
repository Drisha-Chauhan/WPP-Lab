import random

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(n):
    board = [-1] * n
    rows = list(range(n))
    random.shuffle(rows)
    
    for row in rows:
        cols = list(range(n))
        random.shuffle(cols)
        for col in cols:
            if is_safe(board, row, col):
                board[row] = col
                break
        if board[row] == -1:
            return solve_n_queens(n)  
    return board

def print_board(board):
    n = len(board)
    for row in board:
        print("".join("Q" if i == row else "." for i in range(n)))

solution = solve_n_queens(8)
print_board(solution)
