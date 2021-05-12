from collections import defaultdict, deque
from typing import DefaultDict, List, Set, Tuple


def largest_value_in_directed_graph(nodes: str, edges: List[Tuple[int, int]]) -> int:
    """
    A brute-force solution, not efficient. Need to learn more about graph.

    1. Convert given list of tuples into graph adjacency list.
    2. Run DFS starting from each node.
    3. When cycle found, immediately return 0/null.
    4. Otherwise keep track of values for each letter, while traversing the graph.
    """
    graph: DefaultDict[int, List[int]] = defaultdict(deque)

    for source, destination in edges:
        graph[source].append(destination)

    result = 0
    for node in range(len(nodes)):
        value = dfs(graph, nodes, node, set(), defaultdict(int))
        if value == 0:
            return value
        result = max(result, value)

    return result


def dfs(graph: DefaultDict[int, List[int]], nodes: str, vertice: int, visited: Set[int], values: DefaultDict[str, int]) -> int:
    result = 0

    if vertice in visited:
        return result

    visited.add(vertice)
    values[nodes[vertice]] += 1

    if not graph[vertice]:
        return max(values.values())

    for neighbor in graph[vertice]:
        tmp = dfs(graph, nodes, neighbor, visited, values.copy())
        result = max(result, tmp)

    return result


assert largest_value_in_directed_graph("ABACA", [(0, 1),
                                                 (0, 2),
                                                 (2, 3),
                                                 (3, 4)]) == 3

assert largest_value_in_directed_graph("ABACADB", [(0, 1),
                                                   (0, 2),
                                                   (1, 4),
                                                   (2, 3),
                                                   (2, 6),
                                                   (3, 5)]) == 2
