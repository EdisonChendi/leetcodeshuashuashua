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

    def update(self, l, r, h):
        self._update(self.root, l, r, h)

    def _update(self, node, l, r, h):
        if l > node.right or r < node.left:
            return

        if l <= node.left <= node.right <= r:
            if h > node.mx:
                node.mx = h
                node.lazy = True
            return

        self._push_down(node)
        self._update(node.get_left_node(), l, r, h)
        self._update(node.get_right_node(), l, r, h)
        node.mx = max([node.get_left_node().mx, node.get_right_node().mx])

    def _push_down(self, node):
        if not node.lazy or node.left == node.right:
            return

        m = node.mx
        left_node = node.get_left_node()
        if m > left_node.mx:
            left_node.mx = m
            left_node.lazy = not (node.left == node.right)

        right_node = node.get_right_node()
        if m > right_node.mx:
            right_node.mx = m
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
        return max([self._query(node.get_left_node(), l, r), self._query(node.get_right_node(), l, r)])


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # solve by segment tree
        res = []
        segtree = SegmentTree(0, 10**9+1)
        for p,l in positions:
            s,e,h =p,p+l,l
            cur_h = segtree.query(s, e-1)
            segtree.update(s,e-1, h+cur_h)
            res.append(segtree.query(0, 10**9+1))
        return res

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        positions = [[1,2],[4,3],[3,1]]
        expected = [2,3,3]
        self.assertListEqual(sol.fallingSquares(positions), expected)

    def test_case_2(self):
        sol = Solution()
        positions = [[100,100],[200,100]]
        expected = [100,100]
        self.assertListEqual(sol.fallingSquares(positions), expected)

    def test_case_3(self):
        sol = Solution()
        positions = [[1,2],[2,3],[6,1]]
        expected = [2,5,5]
        self.assertListEqual(sol.fallingSquares(positions), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
