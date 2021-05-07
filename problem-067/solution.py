from typing import Dict, OrderedDict
from collections import defaultdict, OrderedDict


class Node:
    def __init__(self, key: str, val: int):
        self.key = key
        self.val = val
        self.freq = 1


class LFUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.node_by_key: Dict[str, Node] = dict()
        self.nodes_by_freq: Dict[int, OrderedDict] = defaultdict(OrderedDict())
        self.min_freq = 0

    def get(self, key: str) -> Node:
        # key not in cache
        if key not in self.node_by_key:
            return -1

        # update internal and return node value
        node = self.node_by_key[key]
        self._update(node)
        return node.val

    def put(self, key: str, value: int) -> None:
        if self.capacity == 0:
            return

        # if already exists, just update the node
        if key in self.node_by_key:
            node = self.node_by_key[key]
            self._update(node)
            node.val = value
        else:
            # handle remove least used node when full
            if self.size == self.capacity:
                node = self.nodes_by_freq[self.min_freq].pop()
                del self.node_by_key[node.key]
                self.size -= 1

            # add node by key and by freq
            node = Node(key, value)
            self.node_by_key[key] = node
            self.nodes_by_freq[1].append(node)
            self.min_freq = 1
            self.size += 1

    def _update(self, node: Node) -> None:
        # remove the node from a freq dict
        freq = node.freq
        self.nodes_by_freq[freq].pop(node)

        # if new max freq reached, then increase min_freq (to handle put when capacity full)
        if self.min_freq == freq and not self.nodes_by_freq[freq]:
            self.min_freq += 1

        # increase freq and add the node to new freq dict
        node.freq += 1
        freq = node.freq
        self.nodes_by_freq[freq].append(node)
