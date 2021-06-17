from typing import Deque, List
from collections import deque
from unittest import TestCase


class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def bfs(root: TreeNode) -> List[int]:
    """
    Simple BFS implementation using queue.
    """
    if not root:
        return None

    queue: Deque[TreeNode] = deque()
    queue.append(root)
    values: List[int] = []

    while queue:
        curr = queue.popleft()
        values.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return values


class Test(TestCase):
    def test(self):
        test_node = TreeNode(1,
                             TreeNode(2,
                                      TreeNode(4),
                                      TreeNode(5)
                                      ),
                             TreeNode(3,
                                      TreeNode(6),
                                      TreeNode(7)
                                      )
                             )
        expected = [1, 2, 3, 4, 5, 6, 7]
        result = bfs(test_node)
        self.assertEqual(expected, result)
