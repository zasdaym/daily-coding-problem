from typing import Dict, List

button_to_chars: List[str] = ["0", "1", "abc", "def",
                              "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def phone_letters(digits: str) -> List[str]:
    # corner case
    if not digits:
        return []

    result: List[str] = [""]

    # for each digit
    for digit in digits:
        tmp: List[str] = []
        chars = button_to_chars[int(digit)]

        # for each char in a button
        for char in chars:
            # add to every existing result
            for i in range(len(result)):
                tmp.append(result[i] + char)
        result = tmp

    return result


tests = [
    "23",
    ""
]

expected_results = [
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
    []
]

for i in range(len(tests)):
    assert sorted(phone_letters(tests[i])) == sorted(expected_results[i])
