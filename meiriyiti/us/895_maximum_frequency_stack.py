import unittest
from typing import List
from pprint import pprint
import collections
import heapq


class FreqStack1:

    def __init__(self):
        self.counter = collections.Counter()
        self.heap = []
        self.id = 0

    def push(self, val: int) -> None:
        if val in self.counter and self.counter[val] > 0:
            self.counter[val] += 1
        else:
            self.counter[val] = 1
        self.id += 1
        heapq.heappush(self.heap, (-self.counter[val], -self.id, val))

    def pop(self) -> int:
        ele = heapq.heappop(self.heap)
        val = ele[2]
        self.counter[val] -= 1
        return val


class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.grouping = collections.defaultdict(list)
        self.counter = collections.Counter()

    def push(self, val: int) -> None:
        freq = self.counter[val] + 1
        self.counter[val] = freq
        self.grouping[freq].append(val)
        self.max_freq = max(self.max_freq, freq)

    def pop(self) -> int:
        v = self.grouping[self.max_freq].pop()
        self.counter[v] -= 1
        if not self.grouping[self.max_freq]:
            self.max_freq -= 1
        return v


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
