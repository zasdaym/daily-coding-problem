from unittest import TestCase


def swap_odd_even_bits(n: int) -> int:
    """
    1. Get all even bits.
    2. Get all odd bits.
    3. Shift the event bits to right, shift the odd bits to left.
    4. Combine both.

    Visualization:
    a b a b a b a b (full bits)

    a 0 a 0 a 0 a 0  (even bits)
    0 b 0 b 0 b 0 b (odd bits)

    0 a 0 a 0 a 0 a (even bits shifted)
    b 0 b 0 b 0 b 0 (odd bits shifted)

    b a b a b a b a (even | odd bits)
    """
    even_mask = 0b10101010
    odd_mask = 0b01010101
    return (n & even_mask) >> 1 | (n & odd_mask) << 1


class Test(TestCase):
    def test(self):
        cases = [
            (0b10101010, 0b01010101),
            (0b11101000, 0b11010100),
        ]
        for case in cases:
            result = swap_odd_even_bits(case[0])
            self.assertEqual(case[1], result)
