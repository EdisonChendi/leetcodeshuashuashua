import unittest
from typing import List
from pprint import pprint
import collections
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = []
        for _, c in collections.Counter(tasks).items():
            heapq.heappush(h, -c)

        f_max = -heapq.heappop(h)
        idle_time = (f_max-1)*n
        while h and idle_time > 0:
            idle_time -= min(f_max-1, -heapq.heappop(h))
        idle_time = max(0, idle_time)
        return idle_time + len(tasks)

    def leastInterval1(self, tasks: List[str], n: int) -> int:
        h, w = [], collections.deque()
        for t, c in collections.Counter(tasks).items():
            heapq.heappush(h, (-c, t))

        tick = 0
        while h or w:
            if w:
                c, t, last = w[0]
                if tick - last > n:
                    w.popleft()
                    heapq.heappush(h, (-c, t))
            if h:
                task = heapq.heappop(h)
                c, t = -task[0], task[1]
                c -= 1
                if c > 0:
                    w.append((c, t, tick))
            tick += 1
        return tick


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        expected = 8
        self.assertEqual(sol.leastInterval(tasks, n), expected)

    def test_case_2(self):
        sol = Solution()
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        expected = 6
        self.assertEqual(sol.leastInterval(tasks, n), expected)

    def test_case_3(self):
        sol = Solution()
        tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
        n = 2
        expected = 16
        self.assertEqual(sol.leastInterval(tasks, n), expected)

    def test_edge_case_1(self):
        sol = Solution()
        tasks = ["A"]
        n = 100
        expected = 1
        self.assertEqual(sol.leastInterval(tasks, n), expected)


if __name__ == "__main__":
    unittest.main()
