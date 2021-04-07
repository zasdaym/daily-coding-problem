from typing import List

def generate_power_set(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = [[]]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            result.append(nums[i:j])
    return result
