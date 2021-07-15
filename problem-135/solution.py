from typing import List
from math import inf


class TreeNode:
    def __init__(self, value: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def min_path_sum(root: TreeNode) -> List[int]:
    # Base case
    if not root:
        return None
    if not root.left and not root.right:
        return [root.value]

    # Get path from both subtree
    left_path = min_path_sum(root.left)
    right_path = min_path_sum(root.right)

    # Default value is set to inf to avoid empty subtree calculated as min sum.
    left_sum, right_sum = inf, inf
    if left_path:
        left_sum = sum(left_path)
    if right_path:
        right_sum = sum(right_path)

    # Insert current value to shorter path
    if left_sum < right_sum:
        return [root.value] + left_path
    else:
        return [root.value] + right_path


test_root = TreeNode(
    10,
    TreeNode(
        5,
        None,
        TreeNode(
            2
        )
    ),
    TreeNode(
        5,
        None,
        TreeNode(
            1,
            TreeNode(-1)
        )
    )
)

got = min_path_sum(test_root)
assert got == [10, 5, 1, -1]
