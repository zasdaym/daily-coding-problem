from typing import List

class Queue:
    def __init__(self):
        self.inbox: List[int] = []
        self.outbox: List[int] = []

    def enqueue(self, val: int):
        self.inbox.append(val)

    def dequeue(self):
        if outbox.empty():
            while not inbox.empty():
                outbox.append(inbox.pop())
        return outbox.pop()
