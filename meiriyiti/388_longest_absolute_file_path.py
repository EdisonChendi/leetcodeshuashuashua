import unittest
from typing import List
from pprint import pprint


class Solution1:
    def lengthLongestPath(self, input: str) -> int:
        res = 0
        N = len(input)

        def dfs(cur, i):
            nonlocal res
            if i == N:
                return

            if input[i] == '\n':
                i += 1

            j = 0
            while i < N and input[i] == '\t':
                i += 1
                j += 1
            cur = cur[:j]

            name = []
            file = False
            while i < N and (input[i] != '\t' and input[i] != '\n'):
                if input[i] == '.':
                    file = True
                name.append(input[i])
                i += 1
            cur.append("".join(name))

            if file:
                res = max(res, len("/".join(cur)))

            dfs(cur, i)

        dfs([], 0)
        return res


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0
        stack = []
        N = len(input)
        i = 0
        while i < N:
            if input[i] == '\n':
                i += 1

            cnt = 0
            while i < N and input[i] == '\t':
                i += 1
                cnt += 1
            for _ in range(len(stack)-cnt):
                stack.pop()

            s = i
            is_file = False
            while i < N and (input[i] != '\t' and input[i] != '\n'):
                if input[i] == '.':
                    is_file = True
                i += 1
            stack.append(i-s)

            if is_file:
                res = max(res, len(stack)-1+sum(stack))
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
        expected = 20
        self.assertEqual(sol.lengthLongestPath(input), expected)

    def test_case_2(self):
        sol = Solution()
        input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
        expected = 32
        self.assertEqual(sol.lengthLongestPath(input), expected)

    def test_case_3(self):
        sol = Solution()
        input = "file1.txt\nfile2.txt\nlongfile.txt"
        expected = 12
        self.assertEqual(sol.lengthLongestPath(input), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
