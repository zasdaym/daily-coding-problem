from typing import List


class Node:
    """
    Node is a binary tree node.
    """

    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_unival_subtrees(root: Node) -> int:
    count, _ = __count_unival_subtress(root, 0)
    return count


def __count_unival_subtress(root: Node, count: List[int]) -> (int, bool):
    """
    Recursively count how many unival trees is exist for every subtree.
    """
    if root is None:
        return 0, True

    left_count, is_left_unival = __count_unival_subtress(root.left, count)
    right_count, is_right_unival = __count_unival_subtress(root.right, count)
    total_count = left_count + right_count

    if not is_left_unival or not is_right_unival:
        return total_count, False

    if root.left and root.value != root.left.value:
        return total_count, False

    if root.right and root.value != root.right.value:
        return total_count, False

    total_count = left_count + right_count + 1
    return total_count, True


node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
assert count_unival_subtrees(node) == 5

#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1
