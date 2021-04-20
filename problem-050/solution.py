class Node:
    def __init__(self, val: str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root: Node) -> int:
    if not root:
        return 0
    elif root.val.isnumeric():
        return int(root.val)

    first_operand = preorder_traversal(root.left)
    second_operand = preorder_traversal(root.right)
    if root.val == "+":
        return first_operand + second_operand
    elif root.val == "-":
        return first_operand - second_operand
    elif root.val == "*":
        return first_operand * second_operand
    elif root.val == "/":
        return first_operand / second_operand

root_node = Node("*", Node("+", Node("3"), Node("2")), Node("+", Node("4"), Node("5")))
assert preorder_traversal(root_node) == 45