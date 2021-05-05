from typing import List


def spiral_visit(nums: List[int]) -> List[int]:
    """
    Simply follow the clockwise flow.
    """
    result: List[int] = []
    if not nums:
        return result

    row_size, col_size = len(nums), len(nums[0])
    row = col = 0
    while row < row_size and col < col_size:
        # get the first row, then move one row below
        for index in range(col, col_size):
            result.append(nums[row][index])
        row += 1

        # get the last column, then move one col back
        for index in range(row, row_size):
            result.append(nums[index][col_size - 1])
        col_size -= 1

        # get the last row, then move one row up
        for index in range(col_size - 1, col - 1, -1):
            result.append(nums[row_size-1][index])
        row_size -= 1

        # get the first col, then move one col forward
        for index in range(row_size - 1, row - 1, -1):
            result.append(nums[index][col])
        col += 1

    return result


test_nums = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]

want = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
got = spiral_visit(test_nums)
assert want == got
