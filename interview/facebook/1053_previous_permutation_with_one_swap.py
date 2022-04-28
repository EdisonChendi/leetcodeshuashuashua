import unittest
from typing import List
from pprint import pprint

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1: return arr
        
        i = len(arr)-2
        while i >= 0 and arr[i] <= arr[i+1]: i -= 1
        
        if i < 0: return arr
        
        j = i
        while j < len(arr)-1 and arr[j+1] < arr[i]: j += 1
        while arr[j] == arr[j-1]: j -= 1
        arr[i],arr[j] = arr[j], arr[i]
        return arr
    
    
'''
[3,2,1]
[1,1,5]
[1,9,4,6,7]
[1,9,4,9,9,10]
'''

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
