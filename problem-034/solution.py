def minimum_palindrome(word: str) -> str:
    """
    Note: This is unoptimal solution.
    Basically there's only 3 cases:
    If first and last char already the same, recurse with the remaining chars.
    If not there's 2 possibilities:
    Recurse with first char stripped.
    Recurse with last char stripped. 
    """
    if len(word) <= 1:
        return word

    if word[0] == word[-1]:
        return word[0] + minimum_palindrome(word[1:-1]) + word[-1]

    back = word[-1] + minimum_palindrome(word[:-1]) + word[-1]
    front = word[0] + minimum_palindrome(word[1:]) + word[0]

    if len(back) < len(front):
        return back
    elif len(back) > len(front):
        return front
    else:
        return min(back, front)


assert minimum_palindrome("abcda") == "abcdcba"
assert minimum_palindrome("google") == "elgoogle"
assert minimum_palindrome("rice") == "ecirice"
