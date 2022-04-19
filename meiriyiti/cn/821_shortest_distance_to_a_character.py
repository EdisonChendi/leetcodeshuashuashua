import unittest
from typing import List
from pprint import pprint


class Solution1:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        N = len(s)
        res = [N]*N
        i = s.find(c)
        while i < N:
            res[i] = 0
            j = i-1
            while j >= 0 and res[j] > i-j:
                res[j] = i-j
                j -= 1
            j = i+1
            while j < N and s[j] != c:
                res[j] = j-i
                j += 1
            i = j
        return res


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        N = len(s)
        res = [N]*N
        dist = N
        for i in range(N):
            if s[i] == c:
                dist = 0
            res[i] = dist
            dist += 1
        dist = N
        for i in reversed(range(N)):
            if s[i] == c:
                dist = 0
            if dist < res[i]:
                res[i] = dist
            dist += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "loveleetcode"
        c = "e"
        expected = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        self.assertListEqual(sol.shortestToChar(s, c), expected)

    def test_case_2(self):
        sol = Solution()
        s = "aaab"
        c = "b"
        expected = [3, 2, 1, 0]
        self.assertListEqual(sol.shortestToChar(s, c), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
