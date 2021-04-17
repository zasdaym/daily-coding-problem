from typing import List


def max_profit(prices: List[int]):
    """
    1. Check if current price is the minimum price so far.
    2. Check current margin (current price - minimum price so far).
    """
    if not prices:
        return 0

    min_price = prices[0]
    max_margin = 0

    for price in prices:
        min_price = min(min_price, price)
        margin = price - min_price
        max_margin = max(max_margin, margin)
    return max_margin


assert max_profit([9, 11, 8, 5, 7, 10]) == 5
