from unittest import TestCase


class ListNode:
    def __init__(self, val: int, prev: 'ListNode' = None, next: 'ListNode' = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

    def append(self, val: int) -> 'ListNode':
        next_node = ListNode(val, self)
        self.next = next_node
        return next_node


def is_palindrome(head: ListNode) -> bool:
    if not head:
        return True

    tail = head
    count = 1
    while tail.next:
        tail = tail.next
        count += 1

    for _ in range(count//2):
        if head.val != tail.val:
            return False
        head = head.next
        tail = tail.prev

    return True


class Test(TestCase):
    def test_odd_nodes(self):
        expected = True
        test_head = ListNode(1)
        curr = test_head
        curr = curr.append(2)
        curr = curr.append(1)
        got = is_palindrome(test_head)
        self.assertEqual(expected, got)

    def test_even_nodes(self):
        expected = True
        test_head = ListNode(1)
        curr = test_head
        curr = curr.append(2)
        curr = curr.append(2)
        curr = curr.append(1)
        got = is_palindrome(test_head)
        self.assertEqual(expected, got)

    def test_not_palindrome(self):
        expected = False
        test_head = ListNode(1)
        curr = test_head
        curr = curr.append(2)
        curr = curr.append(3)
        curr = curr.append(1)
        got = is_palindrome(test_head)
        self.assertEqual(expected, got)
