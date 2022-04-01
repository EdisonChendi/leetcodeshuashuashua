import unittest
from typing import List
from pprint import pprint

import collections
class Solution1:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        if counter[0] % 2 != 0:
            return False
        
        counter[0] = 0

        for n in sorted(counter.keys(), key=abs):
            if counter[n] == 0:
                continue
            if counter[n*2] < counter[n]:
                return False
            counter[n*2] -= counter[n]
            counter[n] = 0

        return True

import collections
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        for n in sorted(counter, key=abs):
            if counter[n*2] < counter[n]:
                return False
            counter[n*2] -= counter[n]
        return True

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [3,1,3,6]
        expected = False
        self.assertEqual(sol.canReorderDoubled(arr), expected)

    def test_case_2(self):
        sol = Solution()
        arr = [2,1,2,6]
        expected = False
        self.assertEqual(sol.canReorderDoubled(arr), expected)

    def test_case_3(self):
        sol = Solution()
        arr = [4,-2,2,-4]
        expected = True
        self.assertEqual(sol.canReorderDoubled(arr), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
