from typing import List


def justify_words(text: str, k: int) -> List[str]:
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
