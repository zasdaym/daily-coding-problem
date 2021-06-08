from typing import Dict, Tuple


def longest_consecutive_length(nums: Tuple[int]) -> int:
    """
    1. If number ever found before, skip it.
    2. If found new number and the neighbor (+1 or -1) was already visited:
        a. Add the num to the bounds cache with updated left bound and right bound.
        b. Update the left bound and right bound of the neighbor.
    3. Check the current sequence bound distance.
    """
    max_length = 0
    bounds: Dict[int, Tuple[int]] = {}
    for num in nums:
        # number already visited
        if num in bounds:
            continue
        left_bound = right_bound = num
        # left neighbor found
        if num - 1 in bounds:
            left_bound = bounds[num-1][0]
        # right_neighbor found
        if num + 1 in bounds:
            right_bound = bounds[num+1][1]

        # add current sequence bounds to cache
        bounds[num] = left_bound, right_bound
        # update neighbor bounds
        bounds[left_bound] = left_bound, right_bound
        bounds[right_bound] = left_bound, right_bound
        # update result
        max_length = max(right_bound - left_bound + 1, max_length)

    return max_length


assert longest_consecutive_length([100, 4, 200, 1, 3, 2]) == 4
