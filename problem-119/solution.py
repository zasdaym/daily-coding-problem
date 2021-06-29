from typing import List, Tuple


def find_covering_interval(intervals: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    Find minimum interval that covers all given intervals.
    """
    if not intervals:
        return None

    max_start, min_end = intervals[0]
    for interval in intervals:
        max_start = max(interval[0], max_start)
        min_end = min(interval[1], min_end)

    result = (min_end, max_start)
    return result


test_intervals = [
    [12, 15],
    [3, 4],
    [2, 6],
    [0, 3],
    [6, 9],
]
expected = (3, 12)
assert find_covering_interval(test_intervals) == expected
