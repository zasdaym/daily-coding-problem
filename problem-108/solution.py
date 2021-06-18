from collections import Counter
from unittest import TestCase


def is_anagram(a: str, b: str) -> bool:
    a_count, b_count = Counter(a), Counter(b)
    return a_count == b_count


class Test(TestCase):
    def test_valid_anagram(self):
        result = is_anagram("abcde", "cdeab")
        self.assertTrue(result)

    def test_invalid_anagram(self):
        result = is_anagram("abcde", "ckeab")
        self.assertFalse(result)
