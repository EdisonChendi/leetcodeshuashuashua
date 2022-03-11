from itertools import product
import unittest
from typing import List
import collections

class Solution1:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        children = collections.defaultdict(list)
        for c,p in enumerate(parents):
            children[p].append(c)

        tree_size = {}
        def dfs(node):
            size = 1 + sum(dfs(child) for child in children[node])
            tree_size[node] = size
            return size

        dfs(-1)
        max_score = 0
        cnt = collections.Counter()
        for i in range(len(parents)):
            score =1
            for child in children[i]:
                score *= tree_size[child]
            if parents[i] != -1:
                score *= tree_size[children[-1][0]] - tree_size[i]
            max_score = max(max_score, score)
            cnt[score] += 1
        return cnt[max_score]

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        children = collections.defaultdict(list)
        for c,p in enumerate(parents):
            children[p].append(c)

        N = len(parents) 
        max_score = -1
        count = 0

        def dfs(n):
            nonlocal max_score, count
            size = 1
            score = 1
            for ch in children[n]:
                ch_size = dfs(ch)
                size += ch_size
                score *= ch_size
            
            if parents[n] != -1:
                score *= N-size
            
            if score > max_score:
                max_score = score
                count = 1
            elif score == max_score:
                count += 1

            return size

        dfs(children[-1][0])
        return count

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        parents = [-1,2,0,2,0]
        expected = 3
        self.assertEqual(sol.countHighestScoreNodes(parents), expected)

    def test_case_2(self):
        sol = Solution()
        parents = [-1,2,0]
        expected = 2
        self.assertEqual(sol.countHighestScoreNodes(parents), expected)

    # def test_edge_case_1(self):
    #     pass



if __name__ == "__main__":
    unittest.main()
