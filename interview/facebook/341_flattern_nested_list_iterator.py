import unittest
from typing import List
from pprint import pprint


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [nestedList]
        self.pointers = [0]
        self._next = None

    def next(self) -> int:
        if self.hasNext():
            res = self._next.getInteger()
            self._next = None
            return res

    def hasNext(self) -> bool:
        if self._next:
            return True

        while self.stack:
            if self.pointers[-1] == len(self.stack[-1]):
                self.pointers.pop()
                self.stack.pop()
            else:
                ele = self.stack[-1][self.pointers[-1]]
                self.pointers[-1] += 1
                if ele.isInteger():
                    self._next = ele
                    break
                else:
                    lst = ele.getList()
                    if len(lst) > 0:
                        self.stack.append(lst)
                        self.pointers.append(0)

        return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
