def is_match(text: str, pattern: str) -> bool:
    """
    Use bottom-up Dynamic Programming solution.
    Create 2d array as cache.
    cache[i][j] means the match result of text[i:] and pattern[j:]
    """
    cache = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
    cache[-1][-1] = True
    for i in range(len(text), -1, -1):
        for j in range(len(pattern) - 1, -1, -1):
            first_match = i < len(text) and pattern[j] in {text[i], '.'}
            if j + 1 < len(pattern) and pattern[j+1] == '*':
                cache[i][j] = cache[i][j+2] or first_match and cache[i+1][j]
            else:
                cache[i][j] = first_match and cache[i+1][j+1]
    return cache[0][0]

assert is_match("abcd", "ab.d")
assert not is_match("abcd", "abed")
assert is_match("abcdef", "ab.*f")