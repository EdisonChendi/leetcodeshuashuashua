from os import openpty
import unittest
from typing import List
from pprint import pprint


class Solution:
    def checkValidString(self, s: str) -> bool:
        def helper(s, sign):
            cnt = 0
            for ch in s:
                if ch == "(":
                    cnt += 1 * sign
                if ch == "*":
                    cnt += 1
                if ch == ")":
                    cnt -= 1 * sign
                if cnt < 0:
                    return False
            return True

        return helper(s, 1) and helper(reversed(s), -1)

    def checkValidString2(self, s: str) -> bool:
        min_count, max_count = 0, 0
        for ch in s:
            if ch == "(":
                min_count += 1
                max_count += 1
            elif ch == ")":
                min_count = max(0, min_count-1)
                max_count -= 1
                if max_count < 0:
                    return False
            else:
                # "*"
                min_count = max(0, min_count-1)
                max_count += 1
        return min_count == 0

    def checkValidString1(self, s: str) -> bool:
        opens, stars = [], []
        for i, ch in enumerate(s):
            if ch == ")":
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            elif ch == "(":
                opens.append(i)
            else:
                stars.append(i)

        while opens and stars:
            o, s = opens.pop(), stars.pop()
            if o > s:
                return False

        return not opens


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "()"
        expected = True
        self.assertEqual(sol.checkValidString(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "(*)"
        expected = True
        self.assertEqual(sol.checkValidString(s), expected)

    def test_case_3(self):
        sol = Solution()
        s = "(*))"
        expected = True
        self.assertEqual(sol.checkValidString(s), expected)

    def test_case_4(self):
        sol = Solution()
        s = "(**)"
        expected = True
        self.assertEqual(sol.checkValidString(s), expected)

    def test_case_5(self):
        sol = Solution()
        s = "(**("
        expected = False
        self.assertEqual(sol.checkValidString(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
