def pow(base: int, exp: int) -> int:
    """
    The trick is called Binary Exponentiation.

    Take example 3^5.
    5 in binary is 101, which can be detailed as 2^2 + 2^0 = 4 + 1.
    So 3^5 = 3^4 + 3^1.
    
    1. Iterate every bit of the exponent from behind, this is done by right shifting the bits on each iteration.
    2. If the current bit is 1, multiply the current result with base.
    3. Square the base on each iteration, because the more to the left, the bigger the number will be.
    """
    if exp < 0:
        base = 1 / base
        exp = -exp
    
    result = 1
    while exp:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    
    return result

assert pow(3, 5) == 243
assert pow(-2, 3) == -8