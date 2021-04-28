from typing import List


def pivoted_binary_search(nums: List[int], target: int) -> int:
    pivot = -1
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            pivot = i

    if target == nums[pivot]:
        return pivot

    if nums[0] <= target:
        return binary_search(nums, 0, pivot-1, target)
    else:
        return binary_search(nums, pivot+1, len(nums)-1, target)


def binary_search(nums: List[int], left: int, right: int, target: int) -> int:
    while left <= right:
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle
        elif target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1


assert pivoted_binary_search([5, 6, 7, 1, 2, 3, 4], 6) == 1
assert pivoted_binary_search([5, 6, 7, 1, 2, 3, 4], 12) == -1
assert pivoted_binary_search([5, 6, 7, 1, 2, 3, 4], 3) == 5
