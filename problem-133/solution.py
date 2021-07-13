from unittest import TestCase


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def append_left(self, value: int):
        new_node = TreeNode(value)
        new_node.parent = self
        self.left = new_node
        return new_node

    def append_right(self, value: int):
        new_node = TreeNode(value)
        new_node.parent = self
        self.right = new_node
        return new_node


def inorder_successor(root: TreeNode) -> TreeNode:
    """
    Two possibilities:
    1. If the given node has right child,
       than the inorder successor must be the smallest/left most node in the right subtree.

    2. Otherwise just track the parent pointer until we found a "up right" pointer.
    """
    if root.right:
        return leftmost(root.right)

    parent = root.parent
    while root != parent.left:
        root, parent = root.parent, parent.parent

    return parent


def leftmost(root: TreeNode) -> TreeNode:
    while root.right:
        root = root.right
    return root


class Test(TestCase):
    def test_inorder_successor(self):
        root = TreeNode(10)

        node_5 = root.append_left(5)
        node_6 = node_5.append_right(6)

        node_30 = root.append_right(30)
        node_22 = node_30.append_left(22)
        node_35 = node_30.append_right(35)

        tests = [
            (node_6, 10),
            (node_5, 6),
            (node_22, 30),
            (node_30, 35),
        ]

        for test in tests:
            self.assertEqual(inorder_successor(test[0]).value, test[1])
