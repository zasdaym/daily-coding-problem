from typing import List

def generate_power_set(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = [[]]
    for num in nums:
        result += [subset + [num] for subset in result]
    return result

got = generate_power_set([1, 2, 3])
expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
assert sorted(got) == expected