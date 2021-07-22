from unittest import TestCase


def is_parantheses_balanced(s: str) -> bool:
    """
    The actual problem is the * char.
    If the char is only ( and ), we can simply track a count.
    The count will increase when ( found, and will decrease if ( found and current count is not 0.

    To solve the * problem, we track two counts.
    The first is if we treat the * as (, named high.
    The second is if we treat the * not as (, named low.
    """
    low, high = 0, 0
    for c in s:
        if c == '(':
            low += 1
            high += 1
        elif c == ')':
            low -= 1
            high -= 1
        else:
            low -= 1
            high += 1

        # Already wrong, exit already.
        if high < 0:
            break

        # We can never have negative values as our "minimal" open parantheses count.
        low = max(low, 0)

    return low == 0


class Test(TestCase):
    def test_is_parantheses_balanced(self):
        tests = [
            ("))))))", False),
            ("()*", True),
            ("(*)", True),
            (")*(", False),
        ]

        for test in tests:
            s, expected = test
            got = is_parantheses_balanced(s)
            self.assertEqual(expected, got)
