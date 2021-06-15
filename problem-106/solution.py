from typing import List


def can_reach_end(hops: List[int]) -> bool:
    steps_left = 1

    for i in range(len(hops) - 1):
        steps_left = max(steps_left - 1, hops[i])
        if steps_left == 0:
            return False
    return True
