from typing import Tuple


class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.left = left
        self.right = right
        self.val = val


def largest_bst_subtree(root: TreeNode) -> TreeNode:
    result = helper(root, 0, None)
    return result[3]


def helper(root: TreeNode, max_size: int, max_root: TreeNode) -> Tuple[int, int, int, TreeNode]:
    if root is None:
        return (0, float('inf'), float('-inf'), max_root)

    left_result = helper(root.left, max_size, max_root)
    left_size, left_min, left_max, _ = left_result

    right_result = helper(root.right, max_size, max_root)
    right_size, right_min, right_max, _ = right_result

    # if root is a valid BST candidate
    if root.val > left_max and root.val < right_min:
        size = left_size + right_size + 1
        if size > max_size:
            max_size = size
            max_root = root
        return (size, min(root.val, left_min), max(root.val, right_max), max_root)
    elif left_size > right_size:
        return left_result
    else:
        return right_result


test_node = TreeNode(1, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(12))
result = largest_bst_subtree(test_node)
assert result.val == 3

#       1
#    3     12
# 2     4
