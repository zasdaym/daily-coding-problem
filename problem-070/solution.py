def digit_sum(num: int) -> int:
    result = 0
    while num > 0 :
        result += num % 10
        num //= 10
    return result
    
def perfect_number(n: int) -> int:
    """
    1. Get the digit sum of given number.
    2. Append a number on the back as string so the digit sum become 10.
    3. Convert back to int.
    """
    diff = 10 - digit_sum(n)
    return int(str(n) + str(diff))

assert perfect_number(1) == 19
assert perfect_number(6) == 64
assert perfect_number(10) == 109
assert perfect_number(11) == 118
assert perfect_number(13) == 136
assert perfect_number(21) == 217
