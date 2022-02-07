import unittest
from typing import List
from pprint import pprint
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = [(-n, ch) for n, ch in ((a, 'a'), (b, 'b'), (c, 'c')) if n > 0]
        heapq.heapify(h)
        res = []
        while h:
            n, ch = heapq.heappop(h)
            if "".join(res[-2:]) == ch+ch:
                if not h:
                    break
                n2, ch2 = heapq.heappop(h)
                res.append(ch2)
                if (-n2)-1 > 0:
                    heapq.heappush(h, (n2+1, ch2))
                heapq.heappush(h, (n, ch))
            else:
                res.append(ch)
                if (-n)-1 > 0:
                    heapq.heappush(h, (n+1, ch))
        return "".join(res)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        a = 1
        b = 1
        c = 7
        expected = "ccaccbcc"
        self.assertEqual(sol.longestDiverseString(a, b, c), expected)

    def test_case_2(self):
        sol = Solution()
        a = 7
        b = 1
        c = 0
        expected = "aabaa"
        self.assertEqual(sol.longestDiverseString(a, b, c), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
