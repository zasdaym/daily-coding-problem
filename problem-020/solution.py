class Node:
    """Node is a singly linked list node."""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_linked_list_intersection(first, second):
    """
    Calculate length of both linked list.
    Forward bigger linked list until have same length as the smalled linked list.
    Iterate until intersection is found.
    """
    first_len, second_len = 0, 0
    first_curr, second_curr = first, second
    
    while first_curr:
        first_len += 1
        first_curr = first_curr.next

    while second_curr:
        second_len += 1
        second_curr = second_curr.next

    diff = first_len - second_len
    if diff < 0:
        diff *= -1
        first, second = second, first
    
    for _ in range(diff):
        first = first.next
    
    while first:
        if first.value == second.value:
            return first.value
        first = first.next
        second = second.next

    return 0

first_linked_list = Node(1, Node(3, Node(5, Node(7, Node(21)))))
second_linked_list = Node(6, Node(12, Node(9, Node(5, Node(7, Node(21))))))

assert find_linked_list_intersection(first_linked_list, second_linked_list) == 5