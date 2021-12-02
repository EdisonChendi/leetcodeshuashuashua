import unittest
from typing import List
from pprint import pprint


class Solution1:
    def maxPower(self, s: str) -> int:
        res = 0
        prev, cur = None, 1
        for ch in s:
            if ch == prev:
                cur += 1
            else:
                res = max(res, cur)
                prev, cur = ch, 1
        return max(res, cur)


class Solution:
    def maxPower(self, s: str) -> int:
        res, cnt = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "tourist"
        expected = 1
        self.assertEqual(sol.maxPower(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "triplepillooooow"
        expected = 5
        self.assertEqual(sol.maxPower(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "abbcccddddeeeeedcba"
        expected = 5
        self.assertEqual(sol.maxPower(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "cc"
        expected = 2
        self.assertEqual(sol.maxPower(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
