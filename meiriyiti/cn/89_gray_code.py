import unittest
from typing import List
from pprint import pprint


class Solution1:
    # https://zhuanlan.zhihu.com/p/29254973
    # https://oi-wiki.org/misc/gray-code/
    # O(2^n)
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(2**n)]


class Solution:
    def grayCode(self, n: int) -> List[int]:
        # a clever method
        # from n -> n+1
        # O(2^n)
        ans = [0, 1]
        for i in range(1, n):
            ans += [v+2**i for v in reversed(ans)]
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 2
        expected = [0, 1, 3, 2]
        self.assertEqual(sol.grayCode(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1
        expected = [0, 1]
        self.assertEqual(sol.grayCode(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
