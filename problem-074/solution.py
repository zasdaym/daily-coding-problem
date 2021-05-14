def solve(n: int, x: int) -> int:
    result = 0

    for i in range(1, n + 1):
        div = x // i
        if x % i == 0 and div >= 1 and div <= n:
            result += 1

    return result

assert solve(6, 12) == 4