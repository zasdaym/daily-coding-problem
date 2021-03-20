from typing import List


def staircase_ways(steps: int, possible_steps: List[int]) -> int:
    """
    Main logic is staircase_ways(3, [1, 2]) = staircase_ways(2, [1, 2]) + staircase_ways(1, [1, 2]).
    Build DP cache bottom up.
    """
    cache = [0 for i in range(steps + 1)]
    cache[0] = 1
    for i in range(steps + 1):
        cache[i] += sum(cache[i - step]
                        for step in possible_steps if i - step > 0)
        cache[i] += 1 if i in possible_steps else 0
    return cache[steps]


assert staircase_ways(6, [1, 3, 5]) == 8
