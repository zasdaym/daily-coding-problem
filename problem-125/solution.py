from typing import Set, Tuple, List


class TreeNode:
    def __init__(self, value: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def two_sum(root: TreeNode, target: int) -> Tuple[int, int]:
    if not root:
        return None

    # convert binary search tree into list
    values: Set[int] = set(dfs(root, []))

    # normal two sum
    for value in values:
        diff = target - value
        if diff in values:
            return value, diff

    return None


def dfs(root: TreeNode, values: List[int]) -> List[int]:
    if not root:
        return values

    values.append(root.value)

    if root.left:
        values = dfs(root.left, values)
    if root.right:
        values = dfs(root.right, values)

    return values


test_node = TreeNode(10,
                     TreeNode(5),
                     TreeNode(15,
                              TreeNode(11),
                              TreeNode(15),
                              )
                     )
two_sum(test_node, 16) == (5, 11)
