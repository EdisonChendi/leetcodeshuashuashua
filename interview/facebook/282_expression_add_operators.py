import unittest
from typing import List
from pprint import pprint


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # use dfs
        N = len(num)
        ord0 = ord('0')

        def dfs(idx, exp, prev, accu, res):
            if idx == N:
                if accu == target:
                    res.append(exp)
                return res

            n = 0
            for i in range(idx, N):
                if i > idx and num[idx] == '0':
                    break
                n = n*10 + ord(num[i])-ord0
                str_n = num[idx:i+1]
                if idx == 0:
                    dfs(i+1, str_n, n, n, res)
                else:
                    dfs(i+1, exp+'+'+str_n, n, accu+n, res)
                    dfs(i+1, exp+'-'+str_n, -n, accu-n, res)
                    dfs(i+1, exp+'*'+str_n, prev*n, accu-prev+prev*n, res)

            return res

        return dfs(0, "", 0, 0, [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = "123"
        target = 6
        expected = ["1*2*3", "1+2+3"]
        self.assertCountEqual(sol.addOperators(num, target), expected)

    def test_case_2(self):
        sol = Solution()
        num = "232"
        target = 8
        expected = ["2*3+2", "2+3*2"]
        self.assertCountEqual(sol.addOperators(num, target), expected)

    def test_case_3(self):
        sol = Solution()
        num = "3456237490"
        target = 9191
        expected = []
        self.assertCountEqual(sol.addOperators(num, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
