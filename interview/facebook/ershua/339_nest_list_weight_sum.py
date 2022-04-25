import unittest
from typing import List
from pprint import pprint
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution1:
    # DFS
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def helper(nestedList, depth):
            res = 0
            for n in nestedList:
                if n.isInteger():
                    res += n.getInteger()*depth
                else:
                    res += helper(n.getList(), depth+1)
            return res

        return helper(nestedList, 1)


class Solution:
    # BFS
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        depth = 0
        q = nestedList
        res = 0
        while q:
            depth += 1
            nxt_q = []
            for n in q:
                if n.isInteger():
                    res += n.getInteger()*depth
                else:
                    nxt_q.extend(n.getList())
            q = nxt_q
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
