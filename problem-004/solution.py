from typing import List


def lowest_missing_positive(numbers: List[int]) -> int:
    """
    Convert given list of numbers into a set.
    Start from 1 and keep increasing until the number is not exist in the set.
    """
    unique_numbers = set(numbers)
    candidate = 1
    while candidate in unique_numbers:
        candidate += 1
    return candidate


assert lowest_missing_positive([3, 4, -1, 1]) == 2
assert lowest_missing_positive([1, 2, 0]) == 3
assert lowest_missing_positive([1, 2, 5, 3, 3]) == 4
