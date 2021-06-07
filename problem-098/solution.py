from typing import List, Set, Tuple


def find_word(board: List[List[str]], target: str) -> bool:
    if not board:
        return False

    row_length = len(board)
    col_length = len(board[0])

    for row in range(row_length):
        for col in range(col_length):
            visited: Set[Tuple[int, int]] = set()
            if search(board, row, col, target, 0, visited):
                return True


def search(board: List[List[str]], row: int, col: int, target: str, target_index: int, visited: Set[Tuple[int, int]]) -> bool:
    if not is_valid(board, row, col):
        return False
    if (row, col) in visited:
        return False
    if board[row][col] != target[target_index]:
        return False
    if target_index == len(target) - 1:
        return True

    visited.add((row, col))

    deltas = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    ]

    for delta in deltas:
        if search(board, row + delta[0], col + delta[1], target, target_index + 1, visited):
            return True

    visited.remove((row, col))
    return False


def is_valid(board: List[List[str]], row: int, col: int) -> bool:
    return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])

test_grid = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

assert find_word(test_grid, 'ABCCED')
assert find_word(test_grid, 'SEE')
assert not find_word(test_grid, 'ABCB')
