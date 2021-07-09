def squareroot(n: int) -> int:
    tolerance = 0.0001
    lo = 0
    hi = n
    guess = (lo + hi) / 2

    while abs(guess ** 2 - n) >= tolerance:
        if guess ** 2 > n:
            hi = guess
        else:
            lo = guess
        guess = (lo + hi) / 2

    return guess


assert squareroot(9) - 3 < 0.0001
assert squareroot(225) - 15 < 0.0001
