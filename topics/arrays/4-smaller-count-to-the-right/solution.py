from bisect import bisect_left, insort


def smaller_count_to_right(nums: List[int]):
    result: List[int] = []
    seen: List[int] = []

    for num in reversed(nums):
        i = bisect_left(seen, num)
        result.append(i)
        insort(seen, num)

    return list(reversed(result))
