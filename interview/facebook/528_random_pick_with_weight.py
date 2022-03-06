import unittest
from typing import List
from pprint import pprint
import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.pre_sums = [w[0], ] + [0, ]*(len(w)-1)
        for i in range(1, len(w)):
            self.pre_sums[i] = w[i]+self.pre_sums[i-1]

    def pickIndex(self) -> int:
        pick = random.randomint(0, self.pre_sums[-1]-1)
        index = bisect.bisect_right(self.pre_sums, pick)
        return self.w[index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
