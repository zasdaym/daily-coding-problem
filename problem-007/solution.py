from typing import Dict

def ways_to_decode(data: str) -> int:
    cache: Dict[str, int] = {}
    return __ways_to_decode(data, cache)

def __ways_to_decode(data: str, cache: Dict[str, int]) -> int:
    if data in cache:
        return cache[data]
    if len(data) <= 2:
        if int(data) < 9 or int(data) > 26:
            return 1
        else:
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
assert ways_to_decode("1121321")  == 16
