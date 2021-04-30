from typing import List


def is_partitionable(nums: List[int]) -> bool:
    # If sum is odd, must be false
    nums_sum = sum(nums)
    if nums_sum % 2 == 1:
        return False

    # The goal is simplified to finding subset whose sum equal is half of the total sum
    target = nums_sum // 2

    # dp[i] = is it possible to create a subset whose sum is equal to i
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        # Like the famous "two sum" problem
        for i in range(target, num-1, -1):
            if i >= num:
                dp[i] = dp[i] or dp[i-num]

    return dp[target]

assert is_partitionable([3, 1, 3, 2, 3, 2])
assert not is_partitionable([1, 3, 7, 8, 2])
