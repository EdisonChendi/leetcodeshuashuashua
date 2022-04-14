import unittest
from typing import List
from pprint import pprint


import functools


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        def num_to_val(num: str) -> int:
            ans = {int(num)}
            for i in range(1, len(num)):
                ans |= {x+y for x in num_to_val(num[:i])
                        for y in num_to_val(num[i:])}
            return ans

        @functools.cache
        def dfs(i, j, diff):
            if i == L1 and j == L2:
                return diff == 0

            if i < L1 and s1[i].isdigit():
                ii = i
                while i < L1 and s1[i].isdigit():
                    i += 1
                for n in num_to_val(s1[ii:i]):
                    if dfs(i, j, diff-n):
                        return True
            elif j < L2 and s2[j].isdigit():
                jj = j
                while j < L2 and s2[j].isdigit():
                    j += 1
                for n in num_to_val(s2[jj:j]):
                    if dfs(i, j, diff+n):
                        return True
            elif diff == 0:
                if i < L1 and j < L2 and s1[i] == s2[j]:
                    return dfs(i+1, j+1, diff)
            elif diff > 0:
                if i < L1:
                    return dfs(i+1, j, diff-1)
            else:
                if j < L2:
                    return dfs(i, j+1, diff+1)
            return False

        L1, L2 = len(s1), len(s2)
        return dfs(0, 0, 0)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s1 = "internationalization"
        s2 = "i18n"
        expected = True
        self.assertEqual(sol.possiblyEquals(s1, s2), expected)

    def test_case_2(self):
        sol = Solution()
        s1 = "l123e"
        s2 = "44"
        expected = True
        self.assertEqual(sol.possiblyEquals(s1, s2), expected)

    def test_case_3(self):
        sol = Solution()
        s1 = "a5b"
        s2 = "c5b"
        expected = False
        self.assertEqual(sol.possiblyEquals(s1, s2), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
