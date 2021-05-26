def min_parantheses_remove(parantheses: str) -> int:
    unclosed = invalid = 0
    for p in parantheses:
        if p == "(":
            unclosed += 1
        elif unclosed == 0:
            invalid += 1
        else:
            unclosed -= 1
    return unclosed + invalid
        