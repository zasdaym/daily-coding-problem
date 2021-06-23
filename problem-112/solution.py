class TreeNode:
    def __init__(self, val: int) -> None:
        self.left: 'TreeNode' = None
        self.right: 'TreeNode' = None
        self.parent: 'TreeNode' = None
        self.val = val


def lca(root: TreeNode, a: TreeNode, b: TreeNode) -> TreeNode:
    # Make both nodes on the same depth
    depth_a, depth_b = depth(a), depth(b)
    if depth_a < depth_b:
        while depth_a < depth_b:
            b = b.parent
            depth_b -= 1
    elif depth_a > depth_b:
        while depth_a > depth_b:
            a = a.parent
            depth_a -= 1

    # Climb both nodes
    while a and b and (a is not b):
        a = a.parent
        b = b.parent

    return a if (a is b) else None


def depth(node: TreeNode) -> int:
    """
    Get given node depth.
    """
    count = 0
    while node:
        count += 1
        node = node.parent
    return count
