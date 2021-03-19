from typing import List


def lowest_missing_positive(numbers: List[int]) -> int:
    unique_numbers = set(numbers)
    candidate = 1
    while candidate in unique_numbers:
        candidate += 1
    return candidate


assert lowest_missing_positive([3, 4, -1, 1]) == 2
assert lowest_missing_positive([1, 2, 0]) == 3
assert lowest_missing_positive([1, 2, 5, 3, 3]) == 4
