from typing import Set, List
from random import randint

def random_with_exception(n: int, nums: List[int]) -> int:
    exclusion: Set[int] = set(nums)
    selection: List[int] = [num for num in range(n) if num not in exclusion]
    return selection[randint(0, len(selection))]

got = random_with_exception(10, [3, 7, 12, 9, 4])
assert got not in [3, 7, 12, 9, 4]