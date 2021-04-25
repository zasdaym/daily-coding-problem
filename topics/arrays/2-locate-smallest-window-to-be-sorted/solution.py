from typing import List, Tuple
from sys import maxsize
from unittest import TestCase


def window(nums: List[int]) -> Tuple[int, int]:
    """
    1. Scan from left to right, keep track of max num so far.
        If current number is less than max num so far, mark it as the end of the window.
    2. Scan from right to left, keep track of min num so far.
        If current number is bigger than min num so far, mark it as the start of the window
    """
    left, right = -1, -1
    n = len(nums)
    max_num, min_num = nums[0], nums[-1]

    for i in range(n):
        max_num = max(max_num, nums[i])
        if max_num > nums[i]:
            right = i

    for i in range(n-1, -1, -1):
        min_num = min(min_num, nums[i])
        if min_num < nums[i]:
            left = i
    
    return (left, right)

class TestSolution(TestCase):
    def test(self):
        got = window([1, 6, 3, 7, 2, 8, 9])
        want = (1, 4)
        self.assertEqual(got, want)
