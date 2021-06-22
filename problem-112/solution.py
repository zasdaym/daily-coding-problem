class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val

def lca(root, a, b):
    def depth(node):
        count = 0
        while node:
            count += 1
            node = node.parent
        return count

    depth_a, depth_b = depth(a), depth(b)
    if depth_a < depth_b:
        while depth_a < depth_b:
            b = b.parent
            depth_b -= 1
    elif depth_a > depth_b:
        while depth_a > depth_b:
            a = a.parent
            depth_a -= 1

    while a and b and (a is not b):
        a = a.parent
        b = b.parent

    return a if (a is b) else None