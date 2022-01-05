import unittest
from typing import List
from pprint import pprint


class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        N = len(s)
        for i in range(N):
            if s[i] != "?":
                continue
            s[i] = 'a'
            if i > 0 and s[i-1] == 'a' or i < N-1 and s[i+1] == 'a':
                s[i] = 'b'
                if i > 0 and s[i-1] == 'b' or i < N-1 and s[i+1] == 'b':
                    s[i] = 'c'
        return "".join(s)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "?zs"
        expected = "azs"
        self.assertEqual(sol.modifyString(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
