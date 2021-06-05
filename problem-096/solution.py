from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
        return [nums]

    permutations: List[List[int]] = []
    for l in permute(nums[1:]):
        for i in range(len(nums)):
            print(permutations)
            permutations.append(l[:i] + [nums[0]] + l[i:])
    
    return permutations
    
permute([1, 2, 3])