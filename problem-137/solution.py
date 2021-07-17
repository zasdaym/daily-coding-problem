from math import ceil
from unittest import TestCase

BITS_PER_INT = 32


class BitArray:
    """
    BitArray is a space efficient array that holds a value of 1 or 0 at each index.
    """

    def __init__(self, size: int) -> None:
        self._size = size
        self._list = [0] * ceil(size / BITS_PER_INT)

    def set(self, i: int, val: int) -> None:
        """
        Set i-th bit as val.
        """
        if not self._is_valid_index(i) or not self._is_valid_val(val):
            return

        list_idx = i // BITS_PER_INT
        int_idx = i % BITS_PER_INT

        # Set only i-th bit to 0 and all remaining to 1.
        mask = ~(1 << int_idx)

        # Set i-th bit to 0 by masking it with above mask, then OR with val at i-th bit.
        self._list[list_idx] = (self._list[list_idx] & mask) | (val << int_idx)

    def get(self, i: int) -> int:
        """
        Get i-th bit.
        """
        if not self._is_valid_index(i):
            return -1

        list_idx = i // BITS_PER_INT
        int_idx = i % BITS_PER_INT

        # Move i-th bit to the right end, AND with 1.
        return (self._list[list_idx] >> int_idx) & 1

    def _is_valid_index(self, i: int) -> bool:
        """
        Check if given index is in valid range.
        """
        return i >= 0 and i < self._size

    def _is_valid_val(self, val: int) -> bool:
        """
        Check if given val is either 0 or 1.
        """
        return val == 0 or val == 1


class Test(TestCase):
    def test_bitarray(self):
        bitarray = BitArray(10)
        bitarray.set(3, 1)
        bitarray.set(6, 1)
        bitarray.set(7, 1)
        bitarray.set(7, 0)
        self.assertEqual(bitarray.get(3), 1)
        self.assertEqual(bitarray.get(6), 1)
        self.assertEqual(bitarray.get(7), 0)
