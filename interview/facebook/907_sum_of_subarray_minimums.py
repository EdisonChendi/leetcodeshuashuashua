import unittest
from typing import List
from pprint import pprint


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        res = 0
        arr.append(-1)
        stack = [-1]
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                idx = stack.pop()
                res += arr[idx]*(i-idx)*(idx-stack[-1])
            stack.append(i)
        return res % MOD


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [3, 1, 2, 4]
        expected = 17
        self.assertEqual(sol.sumSubarrayMins(arr), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
