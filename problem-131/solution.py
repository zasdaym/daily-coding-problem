class ListNode:
    def __init__(self, value: int, next: 'ListNode' = None, random: 'ListNode' = None) -> None:
        self.value = value
        self.next = next
        self.random = random


def clone(head: ListNode) -> ListNode:
    """
    1. Double the given list (a -> b -> c becomes a -> a -> b -> b -> c -> c), but without setting the random attribute on cloned node.
    2. Set cloned node random attribute with the original previous node's random.next
    3. Restore the list by separating the original and the cloned nodes.
    """
    head = double(head)
    set_random_pointers(head)

    dummy_head = head

    while head:
        cloned_next = head.next

        if cloned_next.next:
            head.next, cloned_next.next = head.next.next, cloned_next.next.next
        else:
            head.next, cloned_next.next = head.next.next, None

        head = head.next

    return dummy_head


def double(head: ListNode) -> ListNode:
    dummy_head = head

    while head:
        head.next, head = ListNode(head.value, head.next), head.next

    return dummy_head


def set_random_pointers(head: ListNode) -> None:
    while head:
        head.next.random, head = head.random.next, head.next.next


def is_same_list(a: ListNode, b: ListNode) -> bool:
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.value != b.value:
        return False
    if a.random.value != b.random.value:
        return False
    return is_same_list(a.next, b.next)


node_a = ListNode(1)
node_b = ListNode(2)
node_c = ListNode(3)
node_a.next = node_b
node_a.random = node_c
node_b.next = node_c
node_b.random = node_a
node_c.random = node_b

cloned_head = clone(node_a)
assert is_same_list(node_a, cloned_head)
