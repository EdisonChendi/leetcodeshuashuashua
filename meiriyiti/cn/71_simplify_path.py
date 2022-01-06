import unittest
from typing import List
from pprint import pprint


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != ".":
                stack.append(p)
        return '/' + '/'.join(stack)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        path = "/home/"
        expected = "/home"
        self.assertEqual(sol.simplifyPath(path), expected)

    def test_case_2(self):
        sol = Solution()
        path = "/../"
        expected = "/"
        self.assertEqual(sol.simplifyPath(path), expected)

    def test_case_3(self):
        sol = Solution()
        path = "/home//foo/"
        expected = "/home/foo"
        self.assertEqual(sol.simplifyPath(path), expected)

    def test_case_4(self):
        sol = Solution()
        path = "/home//../foo/"
        expected = "/foo"
        self.assertEqual(sol.simplifyPath(path), expected)

    def test_case_5(self):
        sol = Solution()
        path = "/a/./b/../../c/"
        expected = "/c"
        self.assertEqual(sol.simplifyPath(path), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
