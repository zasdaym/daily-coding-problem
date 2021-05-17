from typing import List, Tuple


def merge_overlap(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not intervals:
        return intervals

    sorted_intervals = sorted(intervals)
    
    stack: List[Tuple[int, int]] = []
    stack.append(sorted_intervals[0])

    for interval in sorted_intervals[1:]:
        last_interval = stack[-1]

        if last_interval[1] < interval[0]:
            stack.append(interval)
        elif last_interval[1] < interval[1]:
            stack[-1][1] = interval[1]

    return stack


test_intervals = [(1, 3), (5, 8), (4, 10), (20, 25)]
print(merge_overlap(test_intervals))
