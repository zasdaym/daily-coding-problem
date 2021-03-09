import ctypes

class Node:
    def __init__(self, val):
        self.val = val
        self.adj = 0

    def __str__(self):
        return f"Value: {self.val}, Adjacent: {self.adj}, Address: {id(self)}"

class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        node = Node(element)
        print(node)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.adj = get_pointer(self.tail)
            self.tail.adj ^= get_pointer(node)
            self.tail = node

    def get(self, index):
        prev_address = 0
        current_node = self.head
        for i in range(index):
            next_address = prev_address ^ current_node.adj
            print(f"next is {next_address}")
            if not next_address:
                return "Index out of range"
            prev_address = get_pointer(current_node)
            current_node = dereference_pointer(next_address)
            print(current_node)
        return current_node.val

def get_pointer(instance):
    return id(instance)

def dereference_pointer(address):
    return ctypes.cast(address, ctypes.py_object).value

xor_linked_list = XORLinkedList()
xor_linked_list.add(1)
xor_linked_list.add(2)
xor_linked_list.add(3)
assert xor_linked_list.get(0) == 1
assert xor_linked_list.get(1) == 2
