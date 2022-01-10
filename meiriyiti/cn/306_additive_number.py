import unittest
from typing import List
from pprint import pprint


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def add(s1: str, s2: str) -> str:
            l1 = len(s1)
            l2 = len(s2)
            i = max(l1, l2)
            s1 = '0'*(i-l1) + s1
            s2 = '0'*(i-l2) + s2
            carry = 0
            res = []
            for i in reversed(range(i)):
                carry, d = divmod(carry + int(s1[i]) + int(s2[i]), 10)
                res.append(str(d))
            if carry:
                res.append(str(carry))
            return ''.join(reversed(res))

        def valid(p1, p2, num):
            if not num:
                return True

            i = max(len(p1), len(p2))
            if len(num) < i:
                return False

            s = add(p1, p2)
            if num.startswith(s):
                return valid(p2, s, num[len(s):])
            return False

        N = len(num)
        if N <= 2:
            return False
        for i in range(1, N//2+1):
            p1 = num[:i]
            if len(p1) > 1 and p1[0] == '0':
                break
            for j in range(i, min(i+N//2+1, N-i)):
                p2 = num[i:j+1]
                if len(p2) > 1 and p2[0] == '0':
                    break
                if valid(p1, p2, num[j+1:]):
                    return True
        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = "112358"
        expected = True
        self.assertEqual(sol.isAdditiveNumber(num), expected)

    def test_case_2(self):
        sol = Solution()
        num = "199100199"
        expected = True
        self.assertEqual(sol.isAdditiveNumber(num), expected)

    def test_case_3(self):
        sol = Solution()
        num = "113"
        expected = False
        self.assertEqual(sol.isAdditiveNumber(num), expected)

    def test_case_4(self):
        sol = Solution()
        num = "198019823962"
        expected = True
        self.assertEqual(sol.isAdditiveNumber(num), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
