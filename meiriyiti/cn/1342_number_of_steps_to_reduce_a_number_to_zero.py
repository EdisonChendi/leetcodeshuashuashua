from cmath import exp
from pwd import struct_passwd
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num > 0:
            if num & 1 == 1:
                num -= 1
            else:
                num >>= 1
            step += 1
        return step


class Solution:
    def numberOfSteps(self, num: int) -> int:
        def cnt_1(num: int) -> int:
            ans = 0
            for i in reversed(range(32)):
                if (num >> i) & 1 == 1:
                    ans += 1
            return ans

        def hightest_1_pos(num: int) -> int:
            for i in reversed(range(32)):
                if (num >> i) & 1 == 1:
                    return i+1
            return -1

        return max(cnt_1(num) + hightest_1_pos(num) - 1, 0)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = 14
        expected = 6
        self.assertEqual(sol.numberOfSteps(num), expected)

    def test_case_2(self):
        sol = Solution()
        num = 8
        expected = 4
        self.assertEqual(sol.numberOfSteps(num), expected)

    def test_case_3(self):
        sol = Solution()
        num = 123
        expected = 12
        self.assertEqual(sol.numberOfSteps(num), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
