from typing import Dict


def longest_substring_with_distinct_char(size: int, string: int) -> int:
    if size > len(string):
        return string

    result = 0
    visited_chars: Dict[str, int] = {}
    left, right = 0, 0
    while left <= right and right < len(string):
        current_char = string[right]

        if current_char not in visited_chars and len(visited_chars) == size:
            left = max(visited_chars.values())
            char_to_remove = string[min(visited_chars.values())]
            visited_chars.pop(char_to_remove)

        visited_chars[current_char] = right
        current_length = right - left + 1
        result = max(result, current_length)
        right += 1
    return result


assert longest_substring_with_distinct_char(2, "abcba") == 3
assert longest_substring_with_distinct_char(2, "abbbbbbbcbadxxaeaav") == 8
