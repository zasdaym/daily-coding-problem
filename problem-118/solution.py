from typing import List


def square_sort(nums: List[int]) -> List[int]:
    squares = [num * num for num in nums]
    return sorted(squares)


test_nums = [-9, -2, 0, 2, 3]
expected = [0, 4, 4, 9, 81]
assert square_sort(test_nums) == expected
