import unittest
from typing import List
from pprint import pprint


# def count(n):
#     res = 0
#     while n > 0:
#         res += n & 1
#         n >>= 1
#     return res


# accu = 0
# for i in range(100):
#     accu += 1
#     cnt = count(i)
#     if cnt == 1:
#         print('-'*100, accu)
#         accu = 0
#     print(cnt)


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        while len(dp) < n+1:
            dp.extend([i+1 for i in dp])
        return dp[:n+1]

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 5
        expected = [0, 1, 1, 2, 1, 2]
        self.assertListEqual(sol.countBits(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 2
        expected = [0, 1, 1]
        self.assertListEqual(sol.countBits(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
