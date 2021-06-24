from typing import List
from re import split
from unittest import TestCase


def reverse(s: str, delimiters: List[str]) -> str:
    words = split('[' + delimiters + ']+', s)
    not_words = split('[^(' + delimiters + ')]+', s)
    print(s, words, not_words)
    if len(words) > 0 and words[-1] == "":
        words = words[:-1]

    words_iterator = reversed(words)

    result: List[str] = []

    for delimiter in not_words:
        result.append(delimiter)
        try:
            result.append(next(words_iterator))
        except StopIteration:
            pass

    return ''.join(result)


class Test(TestCase):
    def test(self):
        test_cases = [
            ("hello/world:here", ":/", "here/world:hello"),
            ("hello/world:here/", ":/", "here/world:hello/"),
            ("hello//world:here", ":/", "here//world:hello"),
        ]

        for test_case in test_cases:
            self.assertEqual(test_case[2], reverse(test_case[0], test_case[1]))
