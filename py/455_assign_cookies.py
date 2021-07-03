import unittest
from typing import List
from pprint import pprint


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi, si, res = 0, 0, 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                res += 1
                gi += 1
            si += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        g = [1, 2, 3]
        s = [1, 1]
        expected = 1
        self.assertEqual(sol.findContentChildren(g, s), expected)

    def test_case_2(self):
        sol = Solution()
        g = [1, 2]
        s = [1, 2, 3]
        expected = 2
        self.assertEqual(sol.findContentChildren(g, s), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
