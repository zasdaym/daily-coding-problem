from typing import List
from unittest import TestCase


def partition(pivot: int, nums: List[int]) -> List[int]:
    smaller: List[int] = []
    equal: List[int] = []
    bigger: List[int] = []
    for num in nums:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            bigger.append(num)
    return smaller + equal + bigger


class Test(TestCase):
    def test_partition(self):
        tests = [
            (10, [9, 12, 3, 5, 14, 10, 10], [9, 3, 5, 10, 10, 12, 14]),
        ]

        for test in tests:
            pivot, nums, expected = test
            got = partition(pivot, nums)
            self.assertEqual(expected, got)
