from typing import List


def count_islands(grid: List[List[int]]) -> int:
    """
    1. Iterate each cell.
    2. If cell is 1:
        1. Iterate each neighbor with dfs until water found or already visited cell found.
    """
    if not grid:
        return 0

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                dfs(grid, row, col)
                count += 1
    return count


def dfs(grid: List[List[int]], row: int, col: int) -> None:
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
        return

    grid[row][col] = 2

    dfs(grid, row+1, col)
    dfs(grid, row-1, col)
    dfs(grid, row, col+1)
    dfs(grid, row, col-1)


test_grid: List[List[int]] = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1]
]
expected_result = 4
assert count_islands(test_grid) == expected_result