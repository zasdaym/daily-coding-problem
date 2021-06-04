from typing import List


def next_permutation(nums: List[int]) -> None:
    """
    1. Iterate from right to left until num on the left is smaller than on the right (this is pivot).
    2. Find the smallest biggest number than the pivot, than swap both positions.
    3. Reverse the sublist from the pivot until the end.
    """
    pivot = len(nums) - 2
    while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
        pivot -= 1

    if pivot >= 0:
        successor = len(nums) - 1
        while successor > 0 and nums[successor] <= nums[pivot]:
            successor -= 1
        swap(nums, pivot, successor)

    reverse(nums, pivot + 1, len(nums) - 1)


def swap(nums: List[int], a: int, b: int) -> None:
    nums[a], nums[b] = nums[b], nums[a]


def reverse(nums: List[int], a: int, b: int) -> None:
    nums[a:b+1] = reversed(nums[a:b+1])


test_nums = [1, 3, 5, 4, 2]
next_permutation(test_nums)
assert test_nums == [1, 4, 2, 3, 5]
