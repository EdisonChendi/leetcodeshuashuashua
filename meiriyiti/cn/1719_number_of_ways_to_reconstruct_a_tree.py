import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        # 构造graph
        neighbors = collections.defaultdict(set)
        for i, j in pairs:
            neighbors[i].add(j)
            neighbors[j].add(i)

        # 找root
        N = len(neighbors)
        root = -1
        for n, neis in neighbors.items():
            # 与所有点都有祖孙关系的是root
            if len(neis) == N-1:
                root = n
                break
        else:
            return 0

        res = 1
        for n, neis in neighbors.items():
            if n == root:
                continue
            # 找parent
            # 祖先 - neis中所有degree比n大的
            # parent - 所有祖先中最小的
            n_degree = len(neis)
            parent_degree = N
            parent = None
            for nei in neis:
                nei_degree = len(neighbors[nei])
                if n_degree <= nei_degree < parent_degree:
                    parent = nei
                    parent_degree = nei_degree

            # 检查parent的合法性
            if not parent or any(nei not in neighbors[parent] for nei in neis if nei != parent):
                print('here!')
                return 0

            # 如果parent和node的degree相等，说明他们位置可以互相交互，则不止1种
            if parent_degree == n_degree:
                res = 2

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pairs = [[1, 2], [2, 3]]
        expected = 1
        self.assertEqual(sol.checkWays(pairs), expected)

    def test_case_2(self):
        sol = Solution()
        pairs = [[1, 2], [2, 3], [1, 3]]
        expected = 2
        self.assertEqual(sol.checkWays(pairs), expected)

    def test_case_3(self):
        sol = Solution()
        pairs = [[1, 2], [2, 3], [2, 4], [1, 5]]
        expected = 0
        self.assertEqual(sol.checkWays(pairs), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
