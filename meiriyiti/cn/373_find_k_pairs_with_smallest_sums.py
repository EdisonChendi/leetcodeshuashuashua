import unittest
from typing import List
from pprint import pprint
import itertools
import heapq
import operator

class Solution1:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        k1 = min(len(nums1), k)
        k2 = min(len(nums2), k)
        return list(map(operator.itemgetter(1), heapq.nsmallest(k, [(nums1[i]+nums2[j], [nums1[i], nums2[j]]) for i, j in itertools.product(range(k1), range(k2))])))

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        L1,L2 = len(nums1),len(nums2)
        h = [(nums1[i]+nums2[0], i, 0) for i in range(min(k,L1))]
        res = []
        while h and len(res) < k:
            _, i, j = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])
            if j + 1 < L2:
                heapq.heappush(h, (nums1[i]+nums2[j+1], i, j + 1))
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums1 = [1,7,11]; nums2 = [2,4,6]; k = 3
        expected = [[1,2],[1,4],[1,6]]
        self.assertCountEqual(sol.kSmallestPairs(nums1, nums2, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums1 = [1,1,2]; nums2 = [1,2,3]; k = 2
        expected = [[1,1],[1,1]]
        self.assertCountEqual(sol.kSmallestPairs(nums1, nums2, k), expected)

    def test_case_3(self):
        sol = Solution()
        nums1 = [1,2]; nums2 = [3]; k = 3
        expected = [[1,3],[2,3]]
        self.assertCountEqual(sol.kSmallestPairs(nums1, nums2, k), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
