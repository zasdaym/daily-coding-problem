from collections import defaultdict
from typing import DefaultDict, List
from bisect import bisect_left


class TimeMap:
    def __init__(self) -> None:
        self.keys: List[int] = []
        self.values: List[int] = []

    def set(self, key: int, value: int) -> None:
        i = bisect_left(self.keys, key)
        if i == len(self.keys):
            self.keys.append(key)
            self.values.append(value)
        elif key == self.keys[i]:
            self.values[i] = value
        else:
            self.keys.insert(i, key)
            self.values.insert(i, value)

    def get(self, key: int) -> int:
        if self.keys is None:
            return None
        i = bisect_left(self.keys, key)
        if len(self.keys) == i:
            return self.values[-1]
        elif self.keys[i] == i:
            return self.values[i]
        elif i == 0:
            return None
        else:
            return self.values[i-1]


class MultiTimeMap:
    def __init__(self) -> None:
        self.time_maps: DefaultDict[int, TimeMap] = defaultdict(TimeMap)

    def set(self, key: int, value: int, time: int) -> None:
        self.time_maps[key].set(time, value)

    def get(self, key: int, time: int) -> int:
        return self.time_maps[key].get(time)


multi_time_map = MultiTimeMap()
multi_time_map.set(1, 1, 0)
multi_time_map.set(1, 2, 2)
assert multi_time_map.get(1, 1) == 1
assert multi_time_map.get(1, 3) == 2

multi_time_map = MultiTimeMap()
multi_time_map.set(1, 1, 5)
multi_time_map.get(1, 0) is None
assert multi_time_map.get(1, 10) == 1

multi_time_map = MultiTimeMap()
multi_time_map.set(1, 1, 0)
multi_time_map.set(1, 2, 0)
assert multi_time_map.get(1, 0) == 2
