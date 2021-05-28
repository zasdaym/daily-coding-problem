from typing import List, Tuple

def division(dividend: int, divisor: int) -> int:
    # determinse sign, will be negative only if one of them is negative.
    sign = -1 if ((dividend < 0)) ^ (divisor < 0) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    # division is just repeated substraction.
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    return sign * quotient


tests: List[Tuple[Tuple[int, int], int]] = [
    ((10, 3), 3),
    ((43, -8), -5),
]

for test in tests:
    assert division(test[0][0], test[0][1]) == test[1]