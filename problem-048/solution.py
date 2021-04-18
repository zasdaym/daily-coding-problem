from typing import List


class Node():
    def __init__(self, val: str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reconstruct_tree(preorder: List[str], inorder: List[str], bound: str = None) -> Node:
    print(bound, preorder, inorder)
    if not inorder or inorder[0] == bound:
        return None

    root = Node(preorder.pop(0))
    root.left = reconstruct_tree(preorder, inorder, root.val)
    inorder.pop(0)
    root.right = reconstruct_tree(preorder, inorder, bound)
    return root


def preorder_traversal(root: Node, vals: List[str] = []) -> List[str]:
    if not root:
        return None

    vals.append(root.val)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

    return vals


reconstructed_root_node = reconstruct_tree(["a", "b", "d", "e", "c", "f", "g"],
                                           ["d", "b", "e", "a", "f", "c", "g"])
assert preorder_traversal(reconstructed_root_node) == ["a", "b", "d", "e", "c", "f", "g"]
