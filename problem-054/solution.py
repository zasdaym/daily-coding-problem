from typing import Dict, List, Tuple

EMPTY = 0

def sudoku(board: List[List[int]]) -> List[List[int]]:
    """
    This is a backtracking solution.
    1. Try to find an empty cell.
    2. Try to assign 1 to 9 in the empty cell, then proceed to next empty cell.
    3. After each assignment, check if the board is still valid (unique on all rows, cols, and boxes).
    4. If after a cell assignment the board is invalid, try another number.
    """
    if is_complete(board):
        return board

    row, col = find_first_empty_cell(board)
    for i in range(1, 10):
        board[row][col] = i
        if is_valid(board):
            result = sudoku(board)
            if is_complete(result):
                return result
        board[row][col] = EMPTY
    return board

def is_complete(board: List[List[int]]) -> bool:
    return all(all(val is not EMPTY for val in row) for row in board)

def find_first_empty_cell(board) -> Tuple[int, int]:
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == EMPTY:
                return i, j
    return -1, -1

def is_valid(board: List[List[int]]) -> bool:
    return are_rows_valid(board) and are_cols_valid(board) and are_boxes_valid(board)

def are_rows_valid(board: List[List[int]]) -> bool:
    for row in board:
        if not is_unique(row):
            return False
    return True

def are_cols_valid(board: List[List[int]]) -> bool:
    for j in range(len(board[0])):
        col = [ board[i][j] for i in range(len(board)) ]
        if not is_unique(col):
            return False
    return True

def are_boxes_valid(board: List[List[int]]) -> bool:
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box: List[int] = []
            for k in range(3):
                for l in range(3):
                    box.append(board[i+k][j+l])
            if not is_unique(box):
                return False
    return True

def is_unique(arr: List[int]) -> bool:
    found: Dict[int, bool] = {}
    for val in arr:
        if val is not EMPTY and val in found:
            return False
        found[val] = True
    return True

def print_board(board: List[List[int]]) -> None:
    for row in board:
        for col in row:
            print(col, end=" ")
        print("")

test_board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

solved_board = sudoku(test_board)
assert is_valid(solved_board)
