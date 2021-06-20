from typing import List
from unittest import TestCase


class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode, path: List[int] = [], paths: List[List[int]] = []) -> List[List[int]]:
    if not root:
        return paths

    new_path = path + [root.val]

    if not root.left and not root.right:
        paths.append(new_path)

    if root.left:
        dfs(root.left, new_path, paths)

    if root.right:
        dfs(root.right, new_path, paths)

    return paths


class Test(TestCase):
    def test(self):
        test_node = TreeNode(1,
                             TreeNode(2),
                             TreeNode(3,
                                      TreeNode(4),
                                      TreeNode(5),
                                      )
                             )
        expected: List[List[int]] = [[1, 2], [1, 3, 4], [1, 3, 5]]
        got = dfs(test_node, [])
        self.assertEqual(expected, got)
