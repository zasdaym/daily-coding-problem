from typing import List


def colorable(graph: List[List[int]], k: int, colors: List[int] = []) -> bool:
    if len(colors) == len(graph):
        return True

    for i in range(k):
        colors.append(i)
        if is_valid(graph, colors):
            if colorable(graph, k, colors):
                return True
            colors.pop()

    return False


def is_valid(graph: List[List[int]], color: List[int]):
    last_vertex, last_color = len(colors) - 1, colors[-1]
    colored_neighbors = [i for i, has_edge in enumerate(
        graph[last_vertex]) if has_edge and i < last_vertex]

    for neighbor in colored_neighbors:
        if colors[neighbor] == last_color:
            return False

    return True
