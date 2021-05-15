from typing import List


def longest_increasing_subsequence_length(nums: List[int]) -> int:
    """
    The key principle is if we found new smallest number, it can be a potential candidate to start new sequence.
    """
    tail_table = [0 for _ in range(len(nums) + 1)]

    tail_table[0] = nums[0]
    result_len = 1

    for i in range(1, len(nums)):
        # Potential new start of subsequence.
        if nums[i] < tail_table[0]:
            tail_table[0] = nums[i]

        # New largest number, just append it to the end of the longest subsequence.
        elif nums[i] > tail_table[result_len-1]:
            tail_table[result_len] = nums[i]
            result_len += 1

        # Tricky part, at first may be not intuitive. Try to print tail_table on every iteration.
        # Simply find the best position to insert the current number into the tail_table.
        # With this trick we lose the possibility to print the result subsequence element
        # because of replacement.
        else:
            insert_pos = binary_search_ceil(
                tail_table, 0, result_len - 1, nums[i])
            tail_table[insert_pos] = nums[i]

    return result_len


def binary_search_ceil(nums: List[int], left: int, right: int, target: int) -> int:
    ceil = -1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] >= target:
            ceil = middle
            right = middle - 1
        else:
            left = middle + 1
    return ceil


test_nums = [2, 5, 1, 7, 11, 8, 10, 13, 6]
assert longest_increasing_subsequence_length(test_nums) == 6
