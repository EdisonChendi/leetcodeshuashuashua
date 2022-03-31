from lzma import is_check_supported
import unittest
from typing import List
from pprint import pprint


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(n):
            N = n
            while n > 0:
                n, r = divmod(n, 10)
                if r == 0 or N % r != 0:
                    return False
            return True

        return [n for n in range(left, right+1) if is_self_dividing(n)]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        left = 1
        right = 22
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        self.assertCountEqual(sol.selfDividingNumbers(left, right), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
