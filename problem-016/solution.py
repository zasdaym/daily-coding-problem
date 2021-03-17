from typing import List

class Logger:
    """Logger saves last N-th order ID"""
    def __init__(self, max_size=1):
        self.order_ids: List[int] = [0] * max_size
        self.current_id = 0

    def record(self, order_id):
        """Add new order ID to Logger"""
        self.order_ids[self.current_id] = order_id
        self.current_id = (self.current_id + 1) % len(self.order_ids)

    def get_last(self, index):
        """Get last index-th order ID"""
        return self.order_ids[(self.current_id - index + len(self.order_ids) % len(self.order_ids))]

logger = Logger(6)
for item in [1, 2, 3, 4, 5, 6]:
    logger.record(item)
assert logger.get_last(1) == 6
