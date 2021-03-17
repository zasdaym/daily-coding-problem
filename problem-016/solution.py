from typing import List
from collections import deque

LIMIT = 5

order_ids = deque()

def record(order_id):
    if len(order_ids) == LIMIT:
        order_ids.popleft()
    order_ids.append(order_id)

def get_last(index):
    return order_ids[-index]

for id in [1, 2, 3, 4, 5, 6]:
    record(id)

assert get_last(1) == 6
