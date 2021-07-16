from typing import List
from collections import deque


def find_largest_rectangle(matrix: List[List[int]]) -> int:
    # Base case
    if not matrix:
        return 0

    row_count, col_count = len(matrix), len(matrix[0])

    # Used to "compress" 1's in all row by column.
    # Count on a column will be reset if 0 is found, because the area must be contiguous.
    one_by_col = [0] * col_count

    largest_area = 0

    for row in matrix:
        for col, val in enumerate(row):
            if val == 0:
                one_by_col[col] = 0
            else:
                one_by_col[col] += 1

        # Calculate maximum area on current row.
        area = infer_area(one_by_col)
        largest_area = max(largest_area, area)

    return largest_area


def infer_area(one_by_col: List[int]) -> int:
    """
    The tricky function.
    Suppose we're given one_by_col like this:
    [1, 0, 2, 2]

    The matrix will be like:
    [1, 0, 1, 1]
    [0, 0, 1, 1]

    How to find the max area? Just brute force all possible subrectangles.
    For every subrectangles we dont't need to check all the 1's,
    because we already "compressed" it.

    The formula to find area for a subrectangle is min_height * width.
    This will automatically set the area to 0 if any col has 0 in it.
    """
    max_area = 0
    for i in range(len(one_by_col)):
        for j in range(i + 1, len(one_by_col) + 1):
            area = min(one_by_col[i:j]) * (j-i)
            max_area = max(max_area, area)
    return max_area


test_matrix = [
    [1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
]

result = find_largest_rectangle(test_matrix)
assert result == 4
