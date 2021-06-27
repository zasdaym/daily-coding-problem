from typing import Deque, Dict, Tuple
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def minimum_level_sum(root: TreeNode) -> int:
    if not root:
        return 0

    queue: Deque[Tuple[TreeNode, int]] = deque()
    queue.append((root, 0))
    sum_by_level: Dict[int, int] = defaultdict(int)

    while queue:
        node, curr_level = queue.popleft()
        sum_by_level[curr_level] += node.val
        if node.left:
            queue.append((node.left, curr_level + 1))
        if node.right:
            queue.append((node.right, curr_level + 1))

    min_level, min_sum = 0, sum_by_level[0]
    for level, sum in sum_by_level.items():
        if sum < min_sum:
            min_level = level

    return min_level

test_node = TreeNode(15, TreeNode(1, TreeNode(4)), TreeNode(2, TreeNode(6), TreeNode(8)))
assert minimum_level_sum(test_node) == 1