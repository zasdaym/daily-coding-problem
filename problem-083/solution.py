class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: TreeNode) -> TreeNode:
    if not root:
        return root
    
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

def is_same_tree(a: TreeNode, b: TreeNode) -> bool:
    if not a and not b:
        return True
    
    if not a or not b:
        return False

    if a.val != b.val:
        return False

    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)    

test_node = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(10, None, TreeNode(18)))
expected = TreeNode(5, TreeNode(10, TreeNode(18)), TreeNode(3, TreeNode(4), TreeNode(1)))
inverted_tree = invert_tree(test_node)
assert is_same_tree(expected, inverted_tree)