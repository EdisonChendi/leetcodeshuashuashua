import unittest
from typing import List
from pprint import pprint


class Solution1:
    def lexicalOrder(self, n: int) -> List[int]:
        N = n
        res = []

        def backtrack(n):

            for k in range(n, n+10 if n != 1 else n+9):
                if k > N:
                    break
                res.append(k)
                if 10*k <= N:
                    backtrack(10*k)

        backtrack(1)
        return res


class Solution2:

    def lexicalOrder(self, n: int) -> List[int]:
        N = n
        res = []

        def dfs(n):
            if n > N:
                return
            res.append(n)
            for i in range(10):
                if n*10+i > N:
                    break
                dfs(n*10+i)

        for i in range(1, 10):
            dfs(i)

        return res


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        j = 1
        for _ in range(n):
            res.append(j)
            if (j*10 <= n):
                j *= 10
            else:
                while j % 10 == 9 or j+1 > n:
                    j //= 10
                j += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 39
        expected = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25,
                    26, 27, 28, 29, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 5, 6, 7, 8, 9]
        self.assertListEqual(sol.lexicalOrder(n), expected)

    # def test_case_2(self):
    #     sol = Solution()
    #     n = 2
    #     expected = [1, 2]
    #     self.assertListEqual(sol.lexicalOrder(n), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
