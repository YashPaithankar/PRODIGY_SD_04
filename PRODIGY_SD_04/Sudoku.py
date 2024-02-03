def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if 'num' is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1  # No empty location found

def solve_sudoku(board):
    row, col = find_empty_location(board)

    # Base case: If no empty location is found, the puzzle is solved
    if row == -1 and col == -1:
        return True

    # Try placing numbers from 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If placing 'num' in the current position doesn't lead to a solution,
            # backtrack and try the next number
            board[row][col] = 0

    # If no number can be placed in the current position, backtrack to the previous position
    return False

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku Puzzle:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku:")
        print_board(sudoku_board)
    else:
        print("\nNo solution exists.")
