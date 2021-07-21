from typing import List
from unittest import TestCase


def min_coins(target: int) -> int:
    coins = [25, 10, 5, 1]
    total_count = 0

    while target:
        # Try to substract the target with each available coins, start with biggest first.
        for coin in coins:
            count = target // coin
            target -= count * coin
            total_count += count

    return total_count


class Test(TestCase):
    def test_min_coins(self):
        tests = [
            (16, 3),
            (70, 4),
            (30, 2),
        ]

        for test in tests:
            target, expected = test
            got = min_coins(target)
            self.assertEqual(expected, got)
