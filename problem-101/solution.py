from typing import Tuple


def prime_sum(num: int) -> Tuple[int, int]:
    for i in range(2, num // 2):
        if is_prime(i) and is_prime(num - i):
            return (i, num - i)
    return None

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5)):
        if num % i == 0:
            return False
    
    return True

assert not is_prime(12)
assert is_prime(13)