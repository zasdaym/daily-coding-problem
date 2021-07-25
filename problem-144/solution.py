from typing import List
from math import inf
from unittest import TestCase


def nearest_larger_number(nums: List[int], i: int) -> int:
    """
    Returns the index of the nearest larger number of the number at index i.
    """

    target = nums[i]
    result_idx, result = None, inf
    for pos, num in enumerate(nums):
        if num > target and num < result:
            result_idx, result = pos, num
    return result_idx


class Test(TestCase):
    def test_nearest_larger_number(self):
        tests = [
            ([4, 1, 3, 5, 6], 0, 3),
            ([4, 9, 3, 5, 6], 1, None),
        ]

        for test in tests:
            nums, i, expected = test
            got = nearest_larger_number(nums, i)
            self.assertEqual(expected, got)
