from random import randint

def biased_toss() -> int:
    n = randint(0, 9)
    if n > 7:
        return 0
    return 1

def unbiased_toss() -> int:
    """
    1. Toss the coin twice.
    2. If the results match, start over, forgetting both results.
    3. If the results differ, use the first result.
    """
    diff = biased_toss() - biased_toss()
    if diff < 0:
        return 0
    if diff > 0:
        return 1
    return unbiased_toss()
