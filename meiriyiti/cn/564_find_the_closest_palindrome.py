import unittest
from typing import List
from pprint import pprint

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        L = len(n)
        num = int(n)

        candidates = [10**(L-1)-1,10**L+1]
        # "83912" -> "891"
        # "8391" -> "83"
        first_half = int(n[:(L+1)//2])
        for h in (first_half-1, first_half, first_half+1):
            x = h if L%2 == 0 else h//10
            while x > 0:
                h = h*10 + x%10
                x //= 10
            candidates.append(h)
        ans = None
        for cand in candidates:
            if cand == num:
                continue
            if ans is None:
                ans = cand
                continue
            diff_cand = abs(cand-num)
            diff_ans = abs(ans-num)
            if diff_cand < diff_ans or diff_cand == diff_ans and cand < ans:
                ans = cand
        return str(ans)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = "123"
        expected = "121"
        self.assertEqual(sol.nearestPalindromic(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = "1"
        expected = "0"
        self.assertEqual(sol.nearestPalindromic(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = "10"
        expected = "9"
        self.assertEqual(sol.nearestPalindromic(n), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
