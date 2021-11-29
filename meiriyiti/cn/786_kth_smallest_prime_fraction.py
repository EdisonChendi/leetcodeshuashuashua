import unittest
from typing import List
from pprint import pprint
from heapq import heappop, heappush

class Solution:
    """
    By merging multiple queues
    arr[0]/arr[1]
    arr[0]/arr[2], arr[1]/arr[2]
    ...
    arr[0]/arr[k], ..., arr[k-1]/arr[k]
    ...
    arr[0]/arr[n-1], ..., arr[n-2]/arr[n-1]
    """
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)
        l = [] 
        for i in range(1, N):
            heappush(l, (arr[0]/arr[i], 0, i))
        
        for _ in range(k-1):
            _, i, j = heappop(l)
            if i+1<j:
                heappush(l, (arr[i+1]/arr[j], i+1, j))

        _, i, j = heappop(l) 
        return [arr[i], arr[j]]


class Solution1:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pass

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [1,2,3,5]; k = 3
        expected = [2,5]
        self.assertListEqual(sol.kthSmallestPrimeFraction(arr,k), expected)

    def test_case_2(self):
        sol = Solution()
        arr = [1,7]; k = 1
        expected = [1,7]
        self.assertListEqual(sol.kthSmallestPrimeFraction(arr,k), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
