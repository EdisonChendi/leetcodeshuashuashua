import unittest
from typing import List
from pprint import pprint

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        s, e = 0, N-1

        def dfs(node, cur, res):
            if node == e:
                res.append(cur[:])
                return res

            for nxt in graph[node]:
                cur.append(nxt)
                dfs(nxt, cur, res)
                cur.pop()

            return res
            
        return dfs(s, [s,], [])

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        graph = [[1,2],[3],[3],[]]
        expected = [[0,1,3],[0,2,3]]
        res = sol.allPathsSourceTarget(graph)
        self.assertCountEqual(res, expected)

    def test_case_2(self):
        sol = Solution()
        graph = [[4,3,1],[3,2,4],[3],[4],[]]
        expected = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
        res = sol.allPathsSourceTarget(graph)
        self.assertCountEqual(res, expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
