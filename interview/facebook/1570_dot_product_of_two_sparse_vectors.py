import unittest
from typing import List
from pprint import pprint

class SparseVector1:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dict = {i:n for i,n in enumerate(nums) if n!=0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        ids = self.dict.keys() & vec.dict.keys()
        return sum(self.dict[id]*vec.dict[id] for id in ids)

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = [(i,n) for i,n in enumerate(nums) if n != 0]

    def dotProduct(self, vec: 'SparseVector') -> int:
        i,j = 0,0
        res = 0
        while i<len(self.nums) and j < len(vec.nums):
            pi,ni = self.nums[i]
            pj,nj = vec.nums[j]
            if pi == pj:
                res += ni*nj
                i += 1
                j += 1
            elif pi < pj:
                i += 1
            else:
                j += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        nums1 = [1,0,0,2,3]
        nums2 = [0,3,0,4,0]
        v1 = SparseVector(nums1)
        v2 = SparseVector(nums2)
        ans = v1.dotProduct(v2)
        expected = 8
        self.assertEqual(ans, expected)

    def test_case_2(self):
        nums1 = [0,1,0,0,0]
        nums2 = [0,0,0,0,2]
        v1 = SparseVector(nums1)
        v2 = SparseVector(nums2)
        ans = v1.dotProduct(v2)
        expected = 0
        self.assertEqual(ans, expected)

    def test_case_3(self):
        nums1 = [0,1,0,0,2,0,0]
        nums2 = [1,0,0,0,3,0,4]
        v1 = SparseVector(nums1)
        v2 = SparseVector(nums2)
        ans = v1.dotProduct(v2)
        expected = 6
        self.assertEqual(ans, expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
