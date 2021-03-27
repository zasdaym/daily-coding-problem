from typing import List


class Node:
    """Node in a linked list."""

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        values: List[int] = []
        curr = self
        while curr:
            values.append(str(curr.value))
            curr = curr.next_node
        return "".join(values)


def remove_last_kth_in_linked_list(head: Node, k: int):
    """
    Maintain two pointers, first on the head, second on the head+k+1.
    Move both pointers until the second one hit the end of the list.
    The first pointer will be in the correct position to do the removal.
    """
    prev_kth = head
    tail = head

    for _ in range(k+1):
        tail = tail.next_node

    while tail:
        tail = tail.next_node
        prev_kth = prev_kth.next_node

    prev_kth.next_node = prev_kth.next_node.next_node


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
remove_last_kth_in_linked_list(head, 2)
assert str(head) == "1235"