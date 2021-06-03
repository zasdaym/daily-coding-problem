from typing import Tuple


class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode) -> int:
    """
    There are 3 possibilities:
    1. Max path sum via the current root
    2. Max path sum is on the left sub-tree
    3. Max path sum is on the right sub-tree

    So on each node, return the max_sum (max possible sum) and root_path_sum (max possible sum via root)
    """
    max_sum, _ = helper(root)
    return max_sum


def helper(root: TreeNode) -> Tuple[int, int]:
    if root is None:
        return (float('-inf'), 0)

    left_max_sum, left_path_sum = helper(root.left)
    right_max_sum, right_path_sum = helper(root.right)

    root_max_sum = max(0, left_path_sum) + root.val + max(0, right_path_sum)
    max_sum = max(left_max_sum, root_max_sum, right_max_sum)
    root_path_sum = max(left_path_sum, right_path_sum, 0) + root.val

    return (max_sum, root_path_sum)

#              7
#        5           25
#    3            24    30
# 1    4
test_node = TreeNode(7, TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4))), TreeNode(25, TreeNode(24), TreeNode(30)))
assert max_path_sum(test_node) == 79