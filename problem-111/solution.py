from typing import List
from collections import Counter
from unittest import TestCase


def anagram_indices(w: str, s: str) -> List[int]:
    """
    For each starting index in s, check every if substring if is an anagram of w.
    """
    result: List[int] = []

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_anagram(w, s[i:j]):
                result.append(i)

    return result


def is_anagram(a: str, b: str) -> bool:
    return Counter(a) == Counter(b)


class Test(TestCase):
    def test(self):
        expected = [0, 3, 4]
        got = anagram_indices("ab", "abxaba")
        self.assertEqual(expected, got)
