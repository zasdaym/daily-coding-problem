from unittest import TestCase

class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = next(self.iterator)

    def peek(self):
        return self._next

    def next(self):
        result = self._next
        self._next = next(self.iterator)
        return result

    def hasNext(self):
        return self._next is not None
