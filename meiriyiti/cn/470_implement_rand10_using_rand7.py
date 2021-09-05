import unittest
from typing import List
from pprint import pprint

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        while True:
            row = rand7()  # 1 - 7, row-1 0-6, (row-1)*7 0-42
            col = rand7()  # 1 - 7
            n = (row-1)*7+col  # 1, 49
            if n <= 40:
                return 1 + (n-1) % 10


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
