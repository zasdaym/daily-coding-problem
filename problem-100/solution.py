from typing import List, Tuple


def cover_points(points: List[Tuple[int, int]]) -> int:
    """
    Iterate point per point and sum all the distance.
    """
    total = 0
    for i in range(len(points) - 1):
        distance = get_min_distance(points[i], points[i + 1])
        total += distance
    return total


def get_min_distance(source: Tuple[int, int], destination: Tuple[int, int]) -> int:
    """
    The minimum number of steps would be to take as many diagonal steps as possible,
    and then move horizontally or vertically. So it can be simplified as max(x_diff, y_diff).
    """
    x_diff = abs(source[0] - destination[0])
    y_diff = abs(source[1] - destination[1])
    return max(x_diff, y_diff)


test_points = [
    (0, 0),
    (1, 1),
    (1, 2),
]
assert cover_points(test_points) == 2

# * * * a *
# * * * * *
# * * * * *
# * * * * *
# * a * * *
# (3, 0)
# (1, 4)
