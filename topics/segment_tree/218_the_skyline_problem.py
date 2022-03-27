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
            if h > node.mx:
                node.mx = h
                node.lazy = True
            return

        self._push_down(node)
        self._update(node.get_left_node(), l, r, h)
        self._update(node.get_right_node(), l, r, h)
        # node.mx = max(node.get_left_node().mx, node.get_right_node().mx)

    def _push_down(self, node):
        if not node.lazy or node.left == node.right:
            return

        left_node = node.get_left_node()
        if node.mx > left_node.mx:
            left_node.mx = node.mx
            left_node.lazy = not (node.left == node.right)

        right_node = node.get_right_node()
        if node.mx > right_node.mx:
            right_node.mx = node.mx
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
        return max(self._query(node.get_left_node(), l, r), self._query(node.get_right_node(), l, r))


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ranges = []
        for l, r, _ in buildings:
            ranges.append(l)
            ranges.append(r)

        ranges.sort()
        seg_tree = SegmentTree(ranges[0], ranges[-1])
        for l, r, h in buildings:
            seg_tree.add(l, r-1, h)

        res = []
        for i in ranges:
            h = seg_tree.query(i, i)
            if not res or res[-1][-1] != h:
                res.append([i, h])
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        buildings = [[2, 9, 10], [3, 7, 15], [
            5, 12, 12], [15, 20, 10], [19, 24, 8]]
        expected = [[2, 10], [3, 15], [7, 12], [
            12, 0], [15, 10], [20, 8], [24, 0]]
        self.assertCountEqual(sol.getSkyline(buildings), expected)

    def test_case_2(self):
        sol = Solution()
        buildings = [[0, 2, 3], [2, 5, 3]]
        expected = [[0, 3], [5, 0]]
        self.assertCountEqual(sol.getSkyline(buildings), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
