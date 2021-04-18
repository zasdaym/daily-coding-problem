from typing import List


class Node():
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reconstruct_tree(preorder: List[str], inorder: List[str]) -> Node:
    def helper(bound: str = None) -> Node:
        if not inorder or inorder[0] == bound:
            return None

        root = Node(preorder.pop(0))
        root.left = helper(root.val)
        inorder.pop(0)
        root.right = helper(bound)
        return root
    return helper()


def inorder_traversal(root: Node, vals: List[str] = []) -> List[str]:
    if root:
        vals.append(root.val)
        inorder_traversal(root.left)
        inorder_traversal(root.right)

    return vals


root_node = Node("a", Node("b", Node("d"), Node("e")),
                 Node("c", Node("f"), Node("g")))
reconsrtucted_root_node = reconstruct_tree(["a", "b", "d", "e", "c", "f", "g"], [
                                           "d", "b", "e", "a", "f", "c", "g"])
# print(inorder_traversal(root_node))
# print(inorder_traversal(reconsrtucted_root_node))
