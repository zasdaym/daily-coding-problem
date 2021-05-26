from typing import List


def lowest_missing_positive(numbers: List[int]) -> int:
    """
    Tricky O(n) time and O(1) space.

    1. Add 0 to the list (more on this later, needed for step 3).
    2. Remove all invalid numbers: lower than 1 and bigger than list length.
    3. Here's the tricky part, count the frequency of number 1 to list length.
    4. Iterate from 1 to list length, return when frequency is 0.
    5. Otherwise return list length.
    """

    numbers.append(0)
    n = len(numbers)
    for i in range(n):
        if numbers[i] < 0 or numbers[i] >= n:
            numbers[i] = 0

    # Using the list index like key in a dict.
    # Because all numbers >= n has been removed, any nums[i] % n is always nums[i].
    # We use this fact to use the list as frequency mapper.
    # So nums[i] / n = the frequency of the number appears in the list.
    for i in range(n):
        numbers[numbers[i]%n] += n

    for i in range(1, n):
        if numbers[i] / n == 0:
            return i
    
    return n


assert lowest_missing_positive([3, 4, -1, 1]) == 2
assert lowest_missing_positive([1, 2, 0]) == 3
assert lowest_missing_positive([1, 2, 5, 3, 3]) == 4
