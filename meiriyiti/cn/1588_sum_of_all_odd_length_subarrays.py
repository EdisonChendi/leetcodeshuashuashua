import unittest
from typing import List
from pprint import pprint


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        return sum(((i+1)*(N-i)+1)//2 * n for i, n in enumerate(arr))

    def sumOddLengthSubarrays2(self, arr: List[int]) -> int:
        res, N = 0, len(arr)
        for i, n in enumerate(arr):
            odd_l, odd_r = (i+1)//2, (N-i)//2
            even_l, even_r = i//2+1, (N-1-i)//2+1
            res += (odd_l*odd_r+even_l*even_r)*n
        return res

    def sumOddLengthSubarrays1(self, arr: List[int]) -> int:
        N = len(arr)+1
        pre_sum = [0, ]*N
        for i in range(1, N):
            pre_sum[i] = pre_sum[i-1] + arr[i-1]
        res = 0
        for arr_len in range(1, N, 2):
            for start in range(N-arr_len):
                res += pre_sum[start+arr_len]-pre_sum[start]
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [1, 4, 2, 5, 3]
        expected = 58
        self.assertEqual(sol.sumOddLengthSubarrays(arr), expected)

    def test_case_2(self):
        sol = Solution()
        arr = [1, 2]
        expected = 3
        self.assertEqual(sol.sumOddLengthSubarrays(arr), expected)

    def test_case_3(self):
        sol = Solution()
        arr = [10, 11, 12]
        expected = 66
        self.assertEqual(sol.sumOddLengthSubarrays(arr), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
