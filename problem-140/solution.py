from typing import List, Set
from unittest import TestCase


def single_elements(numbers: List[int]) -> List[int]:
    """
    Another tricky bit manipulation problem.

    The first step is to filter out all duplicate values by XORing all the numbers (a XOR a is 0).
    Then we get the bits of two unique numbers, this bits is the XOR of the two numbers.
    How to find out the two numbers given the XOR of those two?
    Because the two numbers are distinct, then there must be a 1 bit.

    We can find the where is the rightmost 1 bit by ANDing the bits with -bits. Let's call this position i.
    Then the two unique numbers is the one with i-th bit set (1), and the one with i-th bit not set (0).

    Go through the numbers again. For each number, there are two cases:
        - The i-th bit set.
        - The i-th bit not set.
    XOR all numbers in each "group" to filter out duplicate values in each group.
    """

    # XOR all numbers to find the XOR of the two unique numbers
    xor = 0
    for number in numbers:
        xor ^= number

    # Get the rightmost 1 bit
    xor = xor & -xor

    # XOR all numbers in each group
    result = [0, 0]
    for number in numbers:
        if number & xor:
            result[0] ^= number
        else:
            result[1] ^= number
    return result


class Test(TestCase):
    def test_single_element(self):
        tests = [
            ([2, 4, 6, 8, 10, 2, 6, 10], [4, 8]),
            ([3, 3, 7, 7, 1, 2], [1, 2]),
        ]

        for test in tests:
            numbers, expected = test
            got = single_elements(numbers)
            self.assertEqual(expected, got)
