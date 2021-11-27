import unittest
from typing import List
from pprint import pprint
from math import log, ceil

"""
如何来思考此题？
1. 从x进制来思考
2. x = 猪的状态数量 = 1 + 可以进行的轮数
3. x的r次方 >= buckets
4. r: 猪的数量
5. 每一头猪负责buckets的x进制的1位
6. 例如：第0头猪，负责第0位，第0轮，吃掉编号位0开头的所有桶
                         第1轮，吃掉编号位1开头的所有桶
                         ... 第i轮死掉，说明有毒桶的第0位是i
        第1头猪，负责第1位，第0轮，吃掉该位编号为0的所有桶
                         第1轮，吃掉该位编号位1的所有桶
                         ... 第j轮死掉，说明有毒桶的第1位是i
"""


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest//minutesToDie + 1
        return ceil(log(buckets)/log(states))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        buckets = 1000
        minutesToDie = 15
        minutesToTest = 60
        expected = 5
        self.assertEqual(sol.poorPigs(buckets, minutesToDie, minutesToTest),
                         expected)

    def test_case_1(self):
        sol = Solution()
        buckets = 4
        minutesToDie = 15
        minutesToTest = 15
        expected = 2
        self.assertEqual(sol.poorPigs(buckets, minutesToDie, minutesToTest),
                         expected)

    def test_case_1(self):
        sol = Solution()
        buckets = 4
        minutesToDie = 15
        minutesToTest = 30
        expected = 2
        self.assertEqual(sol.poorPigs(buckets, minutesToDie, minutesToTest),
                         expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
