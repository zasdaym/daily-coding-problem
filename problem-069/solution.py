from typing import List, Set


def max_product_of_three(nums: List[int]) -> int:
    """
    Brute force solution to find maximum product that can be made by multiplying any three integers inside a list.
    """
    result = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                tmp = nums[i] * nums[j] * nums[k]
                result = max(result, tmp)
    return result


assert max_product_of_three([1, 2, 3, 4, 5]) == 60
assert max_product_of_three([1, -2, 3, 4, -5]) == 40
assert max_product_of_three([-10, -10, 5, 2, 1]) == 500
