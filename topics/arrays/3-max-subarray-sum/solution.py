from typing import List
from unittest import TestCase


def max_subarray_sum(nums: List[int]) -> int:
    """
    Kadane algorithm, simply keep track of max sum possible ending at each index,
    Then compare each possibilities.
    """
    max_ending_here = max_so_far = 0
    for num in nums:
        max_ending_here = max(max_ending_here + num, num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def min_subarray_sum(nums: List[int]) -> int:
    """
    Same as max_subarray_sum, just minimum instead maximum.
    """
    min_ending_here = min_so_far = 0
    for num in nums:
        min_ending_here = min(min_ending_here, min_ending_here + num)
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far


def max_circular_subarray_sum(nums: List[int]) -> int:
    """
    For example [8, -1, 3, 4], there will be a minimum subarray that "cuts"
    the maximum circular subarray sum.
    1. Find minimum subarray sum (the "cuts").
    2. Find circular subarray sum = array sum - minimum subarray sum.
    3. Compare circular subarray sum with regular max subarray sum.
    """
    max_wraparound = sum(nums) - min_subarray_sum(nums)
    return max(max_subarray_sum(nums), max_wraparound)


class TestSolution(TestCase):
    def test_max_subarray_sum(self):
        got = max_subarray_sum([34, -50, 42, 14, -5, 86])
        want = 137
        self.assertEqual(got, want)

    def test_max_circular_subarray_sum(self):
        got = max_circular_subarray_sum([8, -1, 4, 3])
        want = 15
        self.assertEqual(got, want)
