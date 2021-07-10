from typing import List
from math import inf


def max_profit(k: int, prices: List[int]) -> int:
    """
    To solve this with the max k transaction rules, we need to consider that max profit with k max transaction
    depends on the max profit with k-1 transaction.

    We build a max_profits 2d array, where max_profits[3][2] means the max profit possible with 3 max transaction
    up to price on index 2.

    On each iteration we need to keep track of max possible profit *AFTER* buying a stock excluding current price.
    Then we use that value to determine whether the current max profit can be obtained by selling at current price
    or just ignore current price.
    """
    max_profits = [[0 for _ in range(len(prices))] for _ in range(k + 1)]

    for i in range(1, k + 1):
        last_profit_after_buy = -inf
        for j in range(1, len(prices)):
            # Last profit after buying a stock before current index.
            last_profit_after_buy = max(
                last_profit_after_buy,
                max_profits[i-1][j-1] - prices[j-1]
            )

            # Take last max profit and ignore current stock, or do new transaction.
            max_profits[i][j] = max(
                max_profits[i][j-1],
                last_profit_after_buy + prices[j]
            )

    return max_profits[k][len(prices)-1]


test_prices = [5, 2, 19, 9, 3, 6, 1, 14, 7, 12]
assert max_profit(2, test_prices) == 30
