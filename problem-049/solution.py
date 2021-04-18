from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    """
    For every number:
    1. Add the current number to positive_sum.
    2. Use positive_sum as max_sum if positive_sum is bigger than max_sum.
    3. Reset positive_sum to 0 if positive_sum is now negative.

    This is named Kadane's algorithm.
    The main priciniple is we can immediately ignore subarray whose sum is negative.
    """
    max_sum, positive_sum = 0, 0
    for num in nums:
        positive_sum += num
        max_sum = max(max_sum, positive_sum)
        if positive_sum < 0:
            positive_sum = 0
    return max_sum

assert max_subarray_sum([34, -50, 42, 14, -5, 86]) == 137