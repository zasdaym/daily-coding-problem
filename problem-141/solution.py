from unittest import TestCase


class Stacks:
    def __init__(self, size: int) -> None:
        self._size = size
        self._list = [0] * size

        first = 0
        middle = size // 2
        back = size - 1
        self._stack_indices = [first, middle, back]

    def pop(self, stack_number: int) -> int:
        if stack_number == 0:
            self._stack_indices[0] -= 1
            return self._list[self._stack_indices[0]]
        elif stack_number == 1:
            self._stack_indices[1] -= 1
            return self._list[self._stack_indices[1]]
        else:
            self._stack_indices[2] += 1
            return self._list[self._stack_indices[2]]

    def push(self, item: int, stack_number: int) -> None:
        if stack_number == 0:
            self._list[self._stack_indices[0]] = item
            self._stack_indices[0] += 1
        elif stack_number == 1:
            self._list[self._stack_indices[1]] = item
            self._stack_indices[1] += 1
        else:
            self._list[self._stack_indices[2]] = item
            self._stack_indices[2] -= 1

        if self._is_resize_needed():
            self._resize()

    def _is_resize_needed(self):
        return self._stack_indices[0] == self._size // 2 or self._stack_indices[1] > self._stack_indices[2]

    def _resize(self):
        self._size *= 2
        prev_list = self._list.copy()
        prev_stack_indices = self._stack_indices.copy()

        self._list = [0] * self._size
        self._stack_indices[0] = 0
        self._stack_indices[1] = self._size // 2
        self._stack_indices[2] = self._size - 1

        for i in range(prev_stack_indices[0]):
            self.push(prev_list[i], 0)

        for i in range(prev_stack_indices[1], prev_stack_indices[2]):
            self.push(prev_list[i], 1)

        for i in range(self._size // 2 - 1, prev_stack_indices[2], -1):
            self.push(prev_list[i], 2)


class Test(TestCase):
    def test_stacks(self):
        stacks = Stacks(10)
        stacks.push(0, 0)
        stacks.push(1, 0)
        stacks.push(2, 0)
        stacks.push(3, 0)
        stacks.push(4, 0)
        stacks.push(5, 1)
        stacks.push(6, 1)
        stacks.push(9, 2)
        stacks.push(8, 2)
        stacks.push(7, 2)

        self.assertEqual(stacks.pop(0), 4)
        self.assertEqual(stacks.pop(0), 3)
        self.assertEqual(stacks.pop(1), 6)
        self.assertEqual(stacks.pop(1), 5)
        self.assertEqual(stacks.pop(2), 7)
