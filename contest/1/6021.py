import unittest
from typing import List
from pprint import pprint


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        f, s = pattern

        def helper(text):
            accu_f = 0
            ans = 0
            for ch in text:
                if ch == s:
                    ans += accu_f
                if ch == f:
                    accu_f += 1
            return ans

        return max(helper(f+text), helper(text+s))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
