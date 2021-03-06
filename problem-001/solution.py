from typing import Dict, List, Set


def two_sum(numbers: List[int], target: int) -> bool:
    """
    Create a set to maintain visited number, because element check in a set is O(1).
    For every number, check if the difference between the target and the number is ever visited.
    """
    visited: Set[int] = set()
    for number in numbers:
        diff = target - number
        if diff in visited:
            return True
        visited.add(number)
    return False


assert two_sum([10, 15, 3, 7], 17)
assert two_sum([1, 2, 3, 4], 4)
assert not two_sum([], 12)
assert not two_sum([1, 2, 3, 4], 12)
