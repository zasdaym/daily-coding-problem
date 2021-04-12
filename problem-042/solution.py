from typing import List


def subset_sum(nums: List[int], target: int) -> List[int]:
    """
    This is a very unoptimal solution.
    Simply generate all the subsets and check if the subset's sum is equal to target.
    """
    subsets = [[]]

    for num in nums:
        subsets += [subset + [num] for subset in subsets]
    for subset in subsets:
        if sum(subset) == target:
            return subset
    return None


assert subset_sum([12, 1, 61, 5, 9, 2], 24) == [12, 1, 9, 2]
