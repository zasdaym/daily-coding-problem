from typing import Tuple


class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def deepest_node(root: TreeNode) -> int:
    if not root:
        return 0

    result: Tuple[TreeNode, int] = dfs(root, 0)
    return result[0]


def dfs(root: TreeNode, depth: int) -> Tuple[TreeNode, int]:
    if not root.left and root.right:
        return root, depth

    left_result = right_result = (root, depth)
    if root.left:
        left_result = dfs(root.left, depth + 1)
    if root.right:
        right_result = dfs(root.right, depth + 1)

    if left_result[1] > right_result[1]:
        return left_result
    else:
        return right_result

test_node = TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(8))
assert deepest_node(test_node).val == 1