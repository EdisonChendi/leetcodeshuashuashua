import unittest
from typing import List
from pprint import pprint


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        N = len(arr)
        indices = [0]*(N+1)
        for i, n in enumerate(arr):
            indices[n] = i

        def reverse(j):
            i = 0
            while i < j:
                # indices[arr[i]], indices[arr[j]] = indices[arr[j]], indices[arr[i]]
                indices[arr[i]], indices[arr[j]] = j, i
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        ans = []
        for i in reversed(range(N)):
            ni = arr[i]
            if ni == i+1:
                continue
            i_idx = indices[i+1]
            reverse(i_idx)
            reverse(i)
            ans.append(i_idx+1)
            ans.append(i+1)

        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [3, 2, 4, 1]
        res = [4, 2, 4, 3]
        self.assertListEqual(sol.pancakeSort(arr), res)

    def test_case_2(self):
        sol = Solution()
        arr = [1, 2, 3]
        res = []
        self.assertEqual(sol.pancakeSort(arr), res)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
