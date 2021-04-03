from typing import List
from heapq import heappop, heappush, heapify


def streaming_median(nums: List[int]) -> List[int]:
    """
    Maintain two groups of numbers, one for the left of the median (smaller)
    and one for the right of the median (bigger).
    Left group is using max heap, while right group is using min heap.
    This way we can use the root of each heap to determine the median.

    The tricky part is we need to keep the difference between two groups
    no more than 1 element.
    """
    result: List[int] = []
    left: List[int] = []
    right: List[int] = []
    heapify(left)
    heapify(right)

    temp_result = 0
    for num in nums:
        if num < temp_result:
            if len(left) - len(right) == 1:
                heappush(right, -1 * heappop(left))
            heappush(left, -1 * num)
        else:
            if len(right) - len(left) == 1:
                heappush(left, -1 * heappop(right))
            heappush(right,  num)

        if len(left) > len(right):
            temp_result = left[0] * -1
        elif len(left) < len(right):
            temp_result = right[0]
        else:
            temp_result = ((left[0] * -1) + right[0]) / 2

        result.append(temp_result)
    return result

assert streaming_median([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]