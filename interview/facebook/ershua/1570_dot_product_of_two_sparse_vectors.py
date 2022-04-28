import unittest
from typing import List
from pprint import pprint

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pos = {i for i,n in enumerate(nums) if n != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        pos = self.pos & vec.pos
        return sum(self.nums[p]*vec.nums[p] for p in pos)
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
