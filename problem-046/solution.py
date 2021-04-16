def longest_palindromic_substring(text: str) -> str:
    """
    1. Check for corner case.
    2. Iterate each char.
        1. Set current index as center position, both as exact position or between two char.
        2. Expand around center, checking if both sides char is still same (palindrome)
    3. Get bigger length of both palindrome.
    4. Set start and end index result position according to the length.
    """
    if not text:
        return ""

    start, end = 0, 0
    for i in range(len(text)):
        odd_length = palindrome_length(text, i, i)
        even_length = palindrome_length(text, i, i + 1)
        max_length = max(odd_length, even_length)
        if max_length > end - start:
            start = i - (max_length - 1) // 2
            end = i + max_length//2

    return text[start:end+1]


def palindrome_length(text: str, left: int, right: int) -> int:
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1
    return right - left - 1


assert longest_palindromic_substring("aabcdcb") == "bcdcb"
assert longest_palindromic_substring("bananas") == "anana"
assert longest_palindromic_substring("slkaakx") == "kaak"
