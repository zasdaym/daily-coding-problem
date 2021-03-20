from typing import List


class Node:
    """
    Node is a binary tree node.
    """

    def __init__(self, val: str, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right


END_MARKER = "end"


def serialize(root: Node) -> str:
    """
    Convert a root of a binary tree into a string representation.
    Just recursively call this function with inorder traversal.
    Each node will be separated by comma.
    """
    if root is None:
        return END_MARKER

    left = serialize(root.left)
    right = serialize(root.right)
    return f"{root.val},{left},{right}"


def deserialize(tree_string: str) -> Node:
    """
    Return the root node of a binary tree given its string representation.
    Split the string representation into list of strings, reverse it, and pass it to helper function.
    """
    values = tree_string.split(",")[::-1]
    return _deserialize(values)


def _deserialize(values: List[str]) -> Node:
    """
    1. Pop last element from the list, create root node.
    2. Generate left and right node recursively.
    """
    if not values:
        return None

    value = values.pop()
    if value == END_MARKER:
        return None

    root = Node(value)
    root.left = _deserialize(values)
    root.right = _deserialize(values)
    return root


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
