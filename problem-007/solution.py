from typing import Dict


def ways_to_decode(data: str) -> int:
    """
    Create a DP cache and pass it to helper function.
    """
    cache: Dict[str, int] = {}
    return __ways_to_decode(data, cache)


def __ways_to_decode(data: str, cache: Dict[str, int]) -> int:
    """
    The logic is: ways_to_decode("1152") = ways_to_decode("1") * ways_to_decode("152") + ways_to_decode("11") * ways_to_decode("52").
    Simplified as single_prefix_result + double_prefix_result.
    double_prefix_result only calculated if the number is between 11 and 26.
    Use a cache to avoid recompute calculated solution.
    """
    if data in cache:
        return cache[data]

    if len(data) <= 2:
        if int(data) < 9 or int(data) > 26:
            return 1
        return 2

    single_prefix_result = ways_to_decode(data[1:])
    cache[data[1:]] = single_prefix_result

    if int(data[:2]) > 26:
        return single_prefix_result

    double_prefix_result = ways_to_decode(data[2:])
    cache[data[2:]] = double_prefix_result

    return single_prefix_result + double_prefix_result


assert ways_to_decode("111") == 3
assert ways_to_decode("4321") == 2
assert ways_to_decode("1121321") == 16
