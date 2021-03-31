from typing import List


def count_trapped_water(walls: List[int]) -> int:
    """
    At every index, the amount of rain water stored
    is the difference between current index height
    and minimum of left max height and right max height.
    """
    left, right = 0, len(walls) - 1
    left_max, right_max = 0, 0
    result = 0

    while left <= right:
        if right_max <= left_max:
            result += max(0, right_max - walls[right])
            right_max = max(right_max, walls[right])
            right -= 1
        else:
            result += max(0, left_max - walls[left])
            left_max = max(left_max, walls[left])
            left += 1

    return result


assert count_trapped_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert count_trapped_water([3, 0, 1, 3, 0, 5]) == 8
