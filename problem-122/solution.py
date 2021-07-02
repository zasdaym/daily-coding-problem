from typing import Dict, List, Tuple


def max_collected_coins(matrix: List[List[int]], row: int = 0, col: int = 0, cache: Dict[Tuple[int, int], int] = None) -> int:
    """
    Find the recursive pattern/structure, find all cases:
    1. The position is on the bottom right: just return the value.
    2. The position is on the bottom row: just move to the right.
    3. The position is on the last col: just move to the bottom.
    4. Otherwise, select max value from moving to the right or moving to the left.
    """
    if cache is None:
        cache = {}

    row_len = len(matrix)
    col_len = len(matrix[0])

    is_bottom = row == row_len - 1
    is_rightmost = col == col_len - 1

    if (row, col) not in cache:
        if is_bottom and is_rightmost:
            cache[row, col] = matrix[row][col]
        elif is_bottom:
            cache[row, col] = matrix[row][col] + \
                max_collected_coins(matrix, row, col + 1, cache)
        elif is_rightmost:
            cache[row, col] = matrix[row][col] + \
                max_collected_coins(matrix, row + 1, col, cache)
        else:
            cache[row, col] = matrix[row][col] + max(max_collected_coins(
                matrix, row + 1, col, cache), max_collected_coins(matrix, row, col + 1, cache))

    return cache[row, col]


test_matrix = [
    [0, 3, 1, 1],
    [2, 0, 0, 4],
    [1, 5, 3, 1],
]
assert max_collected_coins(test_matrix) == 12
