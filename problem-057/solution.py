from typing import List


def justify_words(text: str, k: int) -> List[str]:
    """
    1. Split text into words
    2. Iterate each word:
        1. If word can be appended (total chunk length < k), append it.
        2. If not, append the chunk to the final result immediately, and use the word as new chunk.
    3. if the last temporary string length is < k, append it to the result as the final part.
    """
    if not text:
        return 0

    words = text.split(" ")

    tmp_str, tmp_count = words[0], 1
    result: List[str] = []
    for word in words[1:]:
        if len(tmp_str + word) + 1 <= k:
            tmp_str = f"{tmp_str} {word}"
            tmp_count += 1
        else:
            result.append(tmp_str)
            tmp_str = word
            tmp_count = 1

    if tmp_str:
        result.append(tmp_str)

    return result


test_str = "the quick brown fox jumps over the lazy dog"
expected = ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
assert justify_words(test_str, 10) == expected
