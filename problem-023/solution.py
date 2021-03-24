from typing import List, Tuple
from queue import Queue


class Point:
    """
    Point inside a maze with the distance to the destination.
    """

    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance


def is_valid_coordinate(maze: List[List[bool]], coordinate: Tuple[int, int]) -> bool:
    """
    Check if given coordinate is inside a maze (valid).
    """
    row_length = len(maze)
    col_length = len(maze[0])

    is_valid = not (
        coordinate[0] < 0 or
        coordinate[1] < 0 or
        coordinate[0] >= row_length or
        coordinate[1] >= col_length or
        maze[coordinate[0]][coordinate[1]]
    )
    return is_valid


def count_steps(maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    """
    Create a queue to hold visited Points.
    Create a list of list to mark visited node.
    Check if start coordinate is valid.
    Push the start coordinate to the queue.
    Pop an element from the queue as current coordinate.
    Check if current coordinate is the end coordinate (destination), if yes return the distance immediately.
    Push valid neighbour coordinates to the queue with distance = current distance + 1.
    Repeat popping from the queue until the queue is empty or end coordinate is found.
    """
    visited = [[False] * len(row) for row in maze]
    queue: Queue[Point] = Queue()

    if is_valid_coordinate(maze, start) and not visited[start[0]][start[1]]:
        point = Point(start[0], start[1], 0)
        queue.put(point)
        visited[start[0]][start[1]] = True

    while not queue.empty():
        curr = queue.get()
        if curr.x == end[0] and curr.y == end[1]:
            return curr.distance

        x, y = curr.x, curr.y + 1
        if is_valid_coordinate(maze, [x, y]) and not visited[x][y]:
            queue.put(Point(x, y, curr.distance + 1))

        x, y = curr.x, curr.y - 1
        if is_valid_coordinate(maze, [x, y]) and not visited[x][y]:
            queue.put(Point(x, y, curr.distance + 1))

        x, y = curr.x + 1, curr.y
        if is_valid_coordinate(maze, [x, y]) and not visited[x][y]:
            queue.put(Point(x, y, curr.distance + 1))

        x, y = curr.x - 1, curr.y
        if is_valid_coordinate(maze, [x, y]) and not visited[x][y]:
            queue.put(Point(x, y, curr.distance + 1))

    return -1


matrix = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False]
]
start = (3, 0)
end = (0, 0)
result = count_steps(matrix, start, end)
assert result == 7
