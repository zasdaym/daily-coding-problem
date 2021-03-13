from typing import List

def staircase_ways(steps: int, possible_steps: List[int]) -> int:
    cache = [0 for i in range(steps + 1)]
    cache[0] = 1
    for i in range(steps + 1):
        cache[i] += sum(cache[i - step] for step in possible_steps if i - step > 0)
        cache[i] += 1 if i in possible_steps else 0
    return cache[steps]

assert staircase_ways(6, [1, 3, 5]) == 8
