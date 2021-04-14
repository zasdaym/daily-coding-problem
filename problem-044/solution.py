from typing import List

def count_arr_inversions(nums: List[int]) -> int:
    """
    This is unoptimal solution, simply trying all combinations.
    """
    inversions_count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                inversions_count += 1
    return inversions_count

assert count_arr_inversions([2, 4, 1, 3, 5]) == 3
assert count_arr_inversions([5, 4, 3, 2, 1]) == 10