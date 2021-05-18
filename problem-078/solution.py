from typing import List


class ListNode:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


def merge_sorted_lists(heads: List[ListNode]) -> ListNode:
    """
    Merge pair of sorted linked list.
    For example if 4 linked lists are given, sort heads[0] with heads[3], and heads[1] with heads[2],
    then there is 2 sorted lists, sort it again and that is the single sorted list.
    """
    last = len(heads) - 1

    while last != 0:
        left, right = 0, last
        while left < right:
            heads[left] = merge_two_lists(heads[left], heads[right])
            left += 1
            right -= 1

            if left >= right:
                last = right

    return heads[0]


def merge_two_lists(a: ListNode, b: ListNode) -> ListNode:
    dummy_head = curr = ListNode(0)

    while a and b:
        if a.val < b.val:
            curr.next, curr, a = a, a, a.next
        else:
            curr.next, curr, b = b, b, b.next

    if not a:
        curr.next = b
    elif not b:
        curr.next = a

    return dummy_head.next


def list_values(head: ListNode) -> List[int]:
    result: List[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result

first_test_node = ListNode(1, ListNode(3, ListNode(4, ListNode(12))))
second_test_node = ListNode(2, ListNode(8, ListNode(13, ListNode(14))))
third_test_node = ListNode(2, ListNode(5, ListNode(8, ListNode(13, ListNode(15)))))
test_nodes = [first_test_node, second_test_node, third_test_node]
merged_list = merge_sorted_lists(test_nodes)
list_values(merged_list) == [1, 2, 2, 3, 4, 5, 8, 8, 12, 13, 13, 14, 15]