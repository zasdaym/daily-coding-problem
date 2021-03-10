from typing import List

def max_non_adjacent_sum(numbers: List[int]) -> int:
    if not numbers:
        return 0
    if len(numbers) <= 2:
        return max(numbers[0], numbers[1])

    exclusive_max = 0
    inclusive_max = numbers[0]

    for number in numbers[1:]:
        prev_inclusive_max = inclusive_max
        inclusive_max = max(inclusive_max, exclusive_max + number)
        exclusive_max = prev_inclusive_max

    return max(exclusive_max, inclusive_max)

assert max_non_adjacent_sum([2, 4, 6, 2, 5]) == 13
assert max_non_adjacent_sum([5, 1, 1, 3]) == 8
