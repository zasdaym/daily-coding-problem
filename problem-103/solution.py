from typing import Set
from unittest import TestCase


def shortest_substring(s: str, chars: Set[str]) -> str:
    result = s
    for i in range(len(s) - len(chars)):
        for j in range(len(chars), len(s) + 1):
            complete = True
            for char in chars:
                if char not in s[i:j]:
                    complete = False
                    break
            if complete and len(s[i:j]) < len(result):
                result = s[i:j]
    return result


class Test(TestCase):
    def test_empty(self):
        got = shortest_substring("", set(["a", "e", "i"]))
        want = ""
        self.assertEqual(got, want)

    def test_non_empty(self):
        got = shortest_substring("figehaeci", set(["a", "e", "i"]))
        want = "aeci"
        self.assertEqual(got, want)
