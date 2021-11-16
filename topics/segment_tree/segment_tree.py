import math
import unittest
from typing import List
from pprint import pprint


class Node:

    def __init__(self, l, r, m=None) -> None:
        self.l = l
        self.r = r
        self.m = m


class SegmentTree:

    def __init__(self, arr) -> None:
        self._underling_arr = arr
        self.build(arr)

    def build(self, arr):
        def helper(res, k, l, r):
            node = Node(l, r)
            res[k] = node
            if l == r:
                node.m = arr[l]
                return node.m

            lk, rk = 2*k+1, 2*k+2
            helper(res, lk, l, (l+r)//2)
            helper(res, rk, (l+r)//2+1, r)

            node.m = max(res[lk].m, res[rk].m)
            return res

        l = len(arr)
        tree_len = 2**(math.ceil(math.log(l)/math.log(2))+1)
        self._tree = helper([None]*(tree_len), 0, 0, l-1)

    def update(self, i, v):
        def helper(k, i, v):
            node = self._tree[k]
            if node.l == node.r and node.l == i:
                node.m = v
                return v
            else:
                mid = (node.l+node.r)//2
                m = helper(2*k+1, i, v) if i <= mid else helper(2*k+2, i, v)
                node.m = max(node.m, m)
                return node.m

        helper(0, i, v)

    def query(self, l, r):
        """
        find max btw [l, r] inclusive
        """
        def helper(k, l, r):
            node = self._tree[k]
            if l <= node.l <= node.r <= r:
                return node.m
            mid, lk, rk = (node.l+node.r)//2, 2*k+1, 2*k+2
            mx = -math.inf
            if l <= mid:
                mx = max(mx, helper(lk, l, r))
            if r > mid:
                mx = max(mx, helper(rk, l, r))
            return mx

        return helper(0, l, r)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        st = SegmentTree([5, 3, 7, 2, 14, 1, 6, 4, 8, 15])
        self.assertEqual(st.query(0, 9), 15)
        self.assertEqual(st.query(2, 8), 14)

        st.update(3, 20)
        self.assertEqual(st.query(0, 9), 20)
        self.assertEqual(st.query(1, 8), 20)
        self.assertEqual(st.query(1, 2), 7)
        self.assertEqual(st.query(0, 1), 5)

        st.update(0, 10)
        self.assertEqual(st.query(0, 2), 10)
        self.assertEqual(st.query(0, 1), 10)
        self.assertEqual(st.query(0, 9), 20)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
