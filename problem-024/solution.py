class Node:
    """
    Node in a binary tree.
    """

    def __init__(self, value: int, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self._is_locked = False
        self.locked_descendants_count = 0

    def is_locked(self) -> bool:
        """Return lock status of the node."""
        return self._is_locked

    def _is_lockable_or_unlockable(self) -> bool:
        """
        Check if there is no locked descendants (by count) and parents (iteratively).
        """
        if self.locked_descendants_count > 0:
            return False

        curr = self.parent
        while curr:
            if curr._is_locked:
                return False
            curr = curr.parent
        return True

    def lock(self) -> bool:
        """
        Check if node is lockable, and then add locked descendant count for every parents.
        """
        if self._is_lockable_or_unlockable():
            self._is_locked = True

            curr = self.parent
            while curr:
                curr.locked_descendants_count += 1
                curr = curr.parent
            return True
        else:
            return False

    def unlock(self) -> bool:
        """
        Check if node is unlockable, and then decrease locked descendant count for every parents.
        """
        if self._is_lockable_or_unlockable():
            self._is_locked = False

            curr = self.parent
            while curr:
                curr.locked_descendants_count -= 1
                curr = curr.parent
            return True
        else:
            return False


root_node = Node(0, Node(10, Node(5), Node(9)), Node(
    20, Node(19), Node(25, None, Node(32))))
assert root_node.lock() == True
assert root_node.unlock() == True
