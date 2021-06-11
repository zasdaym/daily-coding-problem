from typing import Dict, List


def continuous_sum(nums: List[int], target: int) -> List[int]:
    """
    1. Track continuous sum for each index on a dict.
    2. When difference of current sum and the target is exists in the dict,
    it means that we can exclude that range and the current sum will be same as the target.
    """
    pos_by_sum: Dict[int, int] = {}
    pos_by_sum[0] = -1
    sum = 0

    for i, num in enumerate(nums):
        sum += num
        pos_by_sum[sum] = i
        diff_pos = pos_by_sum.get(sum - target)
        if diff_pos is not None:
            return nums[diff_pos + 1:i + 1]
    return None


assert continuous_sum([1, 2, 3, 4, 5], 9) == [2, 3, 4]
