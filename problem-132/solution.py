from typing import List
from bisect import bisect_left
from unittest import TestCase


class HitCounter:
    """
    HitCounter keeps track of hits. The hits can be retrieved by specific time range.
    """

    def __init__(self) -> None:
        # Total hits
        self.total_hits = 0

        # Hits by timestamp
        self.hits: List[Tuple[int, int]] = []

    def total(self) -> int:
        """
        Get total hits of the counter.
        """
        return self.total_hits

    def record(self, timestamp: int) -> None:
        """
        Record a hit on given timestamp.
        """
        # Increase total hits
        self.total_hits += 1

        # Convert timestamp to minute, reduce number of elements to store
        minute = timestamp // 60

        # Get insert position to keep the hits sorted by minute
        insert_pos = bisect_left([hit[0] for hit in self.hits], minute)

        if insert_pos < len(self.hits) and self.hits[insert_pos][0] == minute:
            old_hit = self.hits[insert_pos][1]
            self.hits[insert_pos] = (minute, old_hit + 1)
        else:
            self.hits.insert(insert_pos, (minute, 1))

    def range(self, lower: int, upper: int) -> int:
        """
        Get total hits on on specified time range.
        """
        # Convert timestamps to minutes
        lower_minute = lower // 60
        upper_minute = upper // 60

        # Find indices range
        lower_pos = bisect_left([hit[0] for hit in self.hits], lower_minute)
        upper_pos = bisect_left([hit[0] for hit in self.hits], upper_minute)

        # Return the hits sum in given range
        return sum([hit[1] for hit in self.hits[lower_pos:upper_pos + 1]])


class Test(TestCase):
    def setUp(self):
        self.hit_counter = HitCounter()
        self.hit_counter.record(1600000000)
        self.hit_counter.record(1626345815)
        self.hit_counter.record(1626345816)
        self.hit_counter.record(1626345817)

    def test_total(self):
        expected = 4
        got = self.hit_counter.total()
        self.assertEqual(expected, got)

    def test_range(self):
        expected = 3
        got = self.hit_counter.range(1626345810, 1626345820)
        self.assertEqual(expected, got)
