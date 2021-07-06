from typing import List


def rotate(nums: List[int], count: int) -> None:
    """Rotate given list of integers in-place by given count times."""
    count %= len(nums)
    nums[len(nums)-count:], nums[:len(nums)-count] = nums[:count], nums[count:]


test_nums = [1, 2, 3, 4, 5, 6]
rotate(test_nums, 14)
assert test_nums == [3, 4, 5, 6, 1, 2]
