from typing import List


class ListNode:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    prev = None
    while head:
        head.next, head, prev = prev, head.next, head
    return prev


def list_values(head: ListNode) -> List[int]:
    result: List[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result


test_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
assert list_values(reverse_list(test_head)) == [4, 3, 2, 1]
