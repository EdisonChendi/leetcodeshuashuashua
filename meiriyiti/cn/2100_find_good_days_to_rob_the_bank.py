from collections import deque
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        N = len(security)
        if time == 0:
            return list(range(N))
        if time >= N:
            return []

        window_before = deque()
        before = set()
        window_after = deque()
        after = set()
        for i in range(N):
            n = security[i]
            if window_before and n <= window_before[-1]:
                window_before.append(n)
                if len(window_before) > time:
                    window_before.popleft()
                    before.add(i)
            else:
                window_before = deque([n])

            j = N-i-1
            nj = security[j]
            if window_after and nj <= window_after[-1]:
                window_after.append(nj)
                if len(window_after) > time:
                    window_after.popleft()
                    after.add(j)
            else:
                window_after = deque([nj])

        return list(before & after)


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        N = len(security)
        pre = [0]*N
        post = [0]*N
        for i in range(1, N):
            if security[i] >= security[i-1]:
                post[i] = post[i-1]+1

            if security[N-1-i] >= security[N-i]:
                pre[N-1-i] = pre[N-i]+1

        return [k for k in range(time, N-time) if pre[k-time]-pre[k] == time and post[k+time]-post[k] == time]


class TestSolution(unittest.TestCase):

    def test_case_0(self):
        sol = Solution()
        security = [3, 1, 20, 17, 26, 0, 2, 29, 24]
        time = 3
        expected = []
        self.assertCountEqual(sol.goodDaysToRobBank(security, time), expected)

    def test_case_1(self):
        sol = Solution()
        security = [5, 3, 3, 3, 5, 6, 2]
        time = 2
        expected = [2, 3]
        self.assertCountEqual(sol.goodDaysToRobBank(security, time), expected)

    def test_case_2(self):
        sol = Solution()
        security = [1, 1, 1, 1, 1]
        time = 0
        expected = [0, 1, 2, 3, 4]
        self.assertCountEqual(sol.goodDaysToRobBank(security, time), expected)

    def test_case_3(self):
        sol = Solution()
        security = [1, 2, 3, 4, 5, 6]
        time = 2
        expected = []
        self.assertCountEqual(sol.goodDaysToRobBank(security, time), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
