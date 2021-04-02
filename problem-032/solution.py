from typing import List
from math import log


def arbitrage(exchange_rates: List[List[int]]) -> bool:
    """
    The exchange rates can be modelled as a graph.
    Exchange between currency is simply source currency * destination currency.
    So exchange from currency a to b to c to a will be modelled as graph traversal
    a -> b -> c -> a, which in turn will be a * b * c * a.

    So we want to know which cycle in the graph that the product of the values is bigger than 1.
    We can use log to make this easier.
    Because log(a) + log(b) + log(c) + log(a) = log(a * b * c * a),
    to make sure a * b * c * a > 1 we can use -log, because -log(x) will be < 0 if only x < 1
    and the operation between node will be sum, not product anymore.

    This problem turns into finding negative sum cycle, which can be solved using Bellman-Ford algo.  
    """
    # Change all node values to negative log.
    transformed_graph = [[-log(edge) for edge in row]
                         for row in exchange_rates]

    source = 0
    n = len(transformed_graph)
    min_dist = [float('inf')] * n
    min_dist[source] = 0

    for _ in range(n-1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False
