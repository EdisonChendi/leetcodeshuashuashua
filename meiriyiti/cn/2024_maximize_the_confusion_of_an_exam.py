import unittest
from typing import List
from pprint import pprint

class Solution1:
    # LTE
    # O(kn)
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # state: k
        # 0 - consecutive T
        # 1 - consecutive F
        # if answerKey[i] == 'T'
        #   DP[i][k][0] = DP[i-1][k][0]+1
        #   DP[i][k][1] = DP[i-1][k-1][1] + 1
        # else
        #   DP[i][k][0] = DP[i-1][k-1][0]+1
        #   DP[i][k][1] = DP[i-1][k][1] + 1
        res = 0
        N = len(answerKey)
        dpT = [0]*(k+1)
        dpF = [0]*(k+1)
        for i in range(1, N+1):
            new_dpT = [0]*(k+1)
            new_dpF = [0]*(k+1)
            answer = answerKey[i-1]
            for j in range(min(i,k)+1):
                if answer == 'T':
                    new_dpT[j] = dpT[j] + 1
                    if j > 0: new_dpF[j] = dpF[j-1] + 1
                else:
                    if j > 0: new_dpT[j] = dpT[j-1] + 1
                    new_dpF[j] = dpF[j] + 1
                res = max(res, new_dpT[j], new_dpF[j])
            dpT = new_dpT
            dpF = new_dpF
            # print(i, answer, '---'*50)
            # print(f"T:{dpT}")
            # print(f"F:{dpF}")
        return res

import collections

class Solution2:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(tf, k):
            res = 0
            window = collections.deque()
            for ch in answerKey:
                window.append(ch)
                if ch != tf:
                    while k == 0:
                        k += window.popleft() != tf
                k -= ch != tf
                res = max(res, len(window))
            return res

        return max(helper('T', k), helper('F', k))

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # use two pointers
        def helper(tf, k):
            res = 0
            left = right = 0
            for ch in answerKey:
                right += 1
                if ch != tf:
                    while k == 0:
                        k += answerKey[left] != tf
                        left += 1
                k -= ch != tf
                res = max(res, right-left)
            return res

        return max(helper('T', k), helper('F', k))



class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        answerKey = "TTFF"; k = 2
        expected = 4
        self.assertEqual(sol.maxConsecutiveAnswers(answerKey, k), expected)
        
    def test_case_2(self):
        sol = Solution()
        answerKey = "TFFT"; k = 1
        expected = 3
        self.assertEqual(sol.maxConsecutiveAnswers(answerKey, k), expected)

    def test_case_3(self):
        sol = Solution()
        answerKey = "TTFTTFTT"; k = 1
        expected = 5
        self.assertEqual(sol.maxConsecutiveAnswers(answerKey, k), expected)

    def test_case_4(self):
        sol = Solution()
        answerKey = "FTFTTFTT"; k = 2
        expected = 7
        self.assertEqual(sol.maxConsecutiveAnswers(answerKey, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
