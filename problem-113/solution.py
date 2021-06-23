from unittest import TestCase


def reverse_words(s: str) -> str:
    words = list(reversed(s.split(" ")))
    return " ".join(words)


class Test(TestCase):
    def test(self):
        s = "hello world here"
        expected = "here world hello"
        got = reverse_words(s)
        self.assertEqual(expected, got)
