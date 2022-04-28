import unittest
from typing import List
from pprint import pprint

import collections

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal = collections.defaultdict(list)
        s = e = 0
        for i, row in enumerate(nums):
            for j, n in enumerate(row):
                diagonal[i+j].append(n)
                e = max(e, i+j)
                
        res = []
        for d in range(s,e+1):
            res.extend(reversed(diagonal[d]))
            
        return res

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
