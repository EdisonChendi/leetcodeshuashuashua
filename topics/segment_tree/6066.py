import unittest
from typing import List
from pprint import pprint

class Node:
    def __init__(self, l, r) -> None:
        self.mx = 0
        self.left = l
        self.right = r
        self.left_node = None
        self.right_node = None
        self.lazy = False

    def get_left_node(self):
        if self.left_node is None:
            self.left_node = Node(self.left, (self.left+self.right) >> 1)
        return self.left_node

    def get_right_node(self):
        if self.right_node is None:
            self.right_node = Node(
                ((self.left+self.right) >> 1) + 1, self.right)
        return self.right_node


class SegmentTree:

    def __init__(self, l, r) -> None:
        self.root = Node(l, r)

    def add(self, l, r, h):
        self._update(self.root, l, r, h)

    def _update(self, node, l, r, h):
        if l > node.right or r < node.left:
            return

        if l <= node.left <= node.right <= r:
            s = node.right-node.left+1 
            if s > node.mx:
                node.mx = s
                node.lazy = True
            return

        self._push_down(node)
        self._update(node.get_left_node(), l, r, h)
        self._update(node.get_right_node(), l, r, h)
        node.mx = sum([node.get_left_node().mx, node.get_right_node().mx])

    def _push_down(self, node):
        if not node.lazy or node.left == node.right:
            return

        left_node = node.get_left_node()
        left_s = left_node.right-left_node.left+1
        if left_s > left_node.mx:
            left_node.mx = left_s
            left_node.lazy = not (node.left == node.right)

        right_node = node.get_right_node()
        right_s = right_node.right-right_node.left+1
        if right_s > right_node.mx:
            right_node.mx = right_s
            right_node.lazy = not (node.left == node.right)
        node.lazy = False

    def query(self, l, r):
        return self._query(self.root, l, r)

    def _query(self, node, l, r):
        if l > node.right or r < node.left:
            return 0

        if l <= node.left <= node.right <= r:
            return node.mx

        self._push_down(node)
        return sum([self._query(node.get_left_node(), l, r), self._query(node.get_right_node(), l, r)])

class CountIntervals:

    def __init__(self):
        self.segtree = SegmentTree(0, 10**9+1)

    def add(self, left: int, right: int) -> None:
        self.segtree.add(left, right, 1)

    def count(self) -> int:
        return self.segtree.query(0, 10**9+1)



# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

# 输入
# ["CountIntervals", "add", "add", "count", "add", "count"]
# [[], [2, 3], [7, 10], [], [5, 8], []]
# 输出
# [null, null, null, 6, null, 8]


# ["CountIntervals","count","add","count"]
# [[],[],[1,1000000000],[]]

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        cnt = CountIntervals()
        cnt.add(2, 3)
        cnt.add(7, 10)
        self.assertEqual(cnt.count(), 6)
        cnt.add(5, 8)
        self.assertEqual(cnt.count(), 8)

    def test_case_2(self):
        cnt = CountIntervals()
        self.assertEqual(cnt.count(), 0)
        cnt.add(1, 1000000000)
        self.assertEqual(cnt.count(), 1000000000)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
