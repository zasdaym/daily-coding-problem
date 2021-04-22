class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def delete_node(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node(self, node) -> None:
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def move_to_head(self, node) -> None:
        self.delete_node(node)
        self.add_node(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def remove_lru(self) -> int:
        key = self.tail.prev.key
        self.delete_node(self.tail.prev)
        return key

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            new_node = Node(key, value)
            if len(self.cache) >= self.capacity:
                tail = self.remove_lru()
                self.cache.pop(tail)
            self.cache[key] = new_node
            self.add_node(new_node)
        else:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
