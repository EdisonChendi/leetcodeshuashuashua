import unittest
from typing import List
from pprint import pprint

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass


class Solution1:
    # Recursion
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dep_sum(l, depth):
            return sum(depth*ele.getInteger() if ele.isInteger() else dep_sum(ele.getList(), depth+1) for ele in l)

        return dep_sum(nestedList, 1)


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # BFS
        q = nestedList
        res = 0
        depth = 0
        while q:
            depth += 1
            nxt_q = []
            while q:
                ele = q.pop()
                if ele.isInteger():
                    res += depth * ele.getInteger()
                else:
                    nxt_q.extend(ele.getList())
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
