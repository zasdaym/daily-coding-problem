from typing import List

class Node:
    def __init__(self, val: str, left: Node = None, right: Node = None):
        self.val = val
        self.left = left
        self.right = right

END_MARKER = "end"

def serialize(root: Node) -> str:
    if root is None:
        return END_MARKER

    left = serialize(root.left)
    right = serialize(root.right)
    return f"{root.val},{left},{right}"

def deserialize(tree_string: str) -> Node:
    values = tree_string.split(",")[::-1]
    return _deserialize(values)

def _deserialize(values: List[str]) -> Node:
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
