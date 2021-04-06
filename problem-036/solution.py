from typing import List


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def second_largest_in_binary_tree(node: Node) -> int:
    """
    The largest element is the most right node on a binary search tree.
    So there just two possibilities for the 2nd largest element:
    1. Right above the largest element.
    2. The most right element under the largest element left subtree.
    """
    prev = node
    while node.right:
        prev = node
        node = node.right

    if not node.left:
        return prev

    node = node.left
    while node.right:
        node = node.right

    return node.value

root = Node(5, Node(2, Node(1), Node(3)),
            Node(12, Node(9, Node(7, Node(6), Node(10)), Node(11))))
assert second_largest_in_binary_tree(root) == 11
