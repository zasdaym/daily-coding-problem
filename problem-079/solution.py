from typing import List


def non_decreasing_nums(nums: List[int]) -> bool:
    """
    1. Find i where nums[i-1] > nums[i].
    2. There is two possibilities, change the nums[i-1] or nums[i].
    3. Change nums[i-1] when nums[i] is bigger than all numbers behind nums[i-1].
    4. Otherwise change nums[i]
    """
    count = 0
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            count += 1
            if count > 2:
                return False
            if i < 2 or nums[i-2] <= nums[i]:
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i-1]
    return count <= 1


tests = [
    [10, 5, 7],
    [10, 5, 1],
    [3, 10, 2, 4],
    [3, 10, 4],
]

expected_results = [
    True,
    False,
    False,
    True
]

for i in range(len(tests)):
    assert non_decreasing_nums(tests[i]) == expected_results[i]
