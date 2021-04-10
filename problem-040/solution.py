from typing import List

def single_number(nums: List[int]) -> int:
    """
    This is a tricky bit manipulation solution.
    1. Variable ones will hold bits of visited numbers that appears once so far.
    2. Variable twos will hold bits of visited numbers that appears twice so far.
    3. For every iteration
        1. Add the common bits of ones and current number to twos.
        2. XOR ones with current number. XOR will filter out duplicate number.
        3. Remove common 1 bits of ones and twos, which means the number has appeared three times.
    """
    ones = 0
    twos = 0

    for num in nums:
        # Record number that appears twice.
        twos |= (ones & num)

        # Record number that appears once.
        ones ^= num

        # Remove number that is on ones and twos.
        common_bit_mask = ~(ones & twos)
        ones &= common_bit_mask
        twos &= common_bit_mask
    return ones

assert single_number([6, 1, 3, 3, 3, 6, 6]) == 1