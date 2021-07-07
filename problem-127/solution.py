class ListNode:
    def __init__(self, value: int, next: 'ListNode' = None) -> None:
        self.value = value
        self.next = next

def sum_linked_list(a: ListNode, b: ListNode) -> int:
    return list_to_int(a) + list_to_int(b)

def list_to_int(head: ListNode) -> int:
    result = 0
    multiplier = 1
    while head:
        result += (head.value * multiplier)
        multiplier *= 10
        head = head.next
    return result

test_a = ListNode(1, ListNode(2, ListNode(3)))
test_b = ListNode(4, ListNode(1, ListNode(1, ListNode(1))))
result = sum_linked_list(test_a, test_b)
assert result == 1435