from typing import List


def find_word(grid: List[List[str]], target: str) -> bool:
    if not grid:
        return False

    row_length = len(grid)
    col_length = len(grid[0])

    for row in range(row_length):
        word = ""
        for char in grid[row]:
            word += char
        if target in word:
            return True

    for col in range(col_length):
        word = ""
        for row in range(row_length):
            char = grid[row][col]
            word += char
        if target in word:
            return True

    return False


test_grid = [
    ['b', 'c', 'x', 'g', 'u'],
    ['a', 'z', 'p', 'e', 'a'],
    ['i', 'f', 'o', 'a', 't'],
    ['q', 'z', 'x', 'r', 'f'],
]
test_target = "gear"
assert find_word(test_grid, test_target)
