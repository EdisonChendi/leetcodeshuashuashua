import unittest
from typing import List
from pprint import pprint


class RangeSumSegmentTree:

    def __init__(self, arr) -> None:
        self._arr = arr
        self.tree = [0]*(4*len(self._arr))
        self.lazy = [0]*(4*len(self._arr))
        self.build()

    def build(self):

        def _build(tree_index, lo, hi):
            if lo == hi:
                self.tree[tree_index] = self._arr[lo]
                return self.tree[tree_index]

            mid = (lo+hi) >> 1
            l = _build(2*tree_index+1, lo, mid)
            r = _build(2*tree_index+2, mid+1, hi)
            self.tree[tree_index] = l + r
            return self.tree[tree_index]

        _build(0, 0, len(self._arr)-1)

    def add(self, arr_index, val):
        self.range_add(arr_index, arr_index, val)

    def _lazy(self, tree_index, tree_lo, tree_hi, val):
        self.tree[tree_index] += (tree_hi-tree_lo+1)*val
        self.lazy[tree_index] += val

    def _push_down(self, tree_index, tree_lo, tree_hi):
        if self.lazy[tree_index] == 0:
            return
        mid = (tree_lo+tree_hi) >> 1
        self._lazy(2*tree_index+1, tree_lo, mid, self.lazy[tree_index])
        self._lazy(2*tree_index+2, mid+1, tree_hi, self.lazy[tree_index])
        self.lazy[tree_index] = 0

    def range_add(self, arr_lo, arr_hi, val):
        def _range_add(tree_index, tree_lo, tree_hi, arr_lo, arr_hi, val):
            if arr_hi < tree_lo or arr_lo > tree_hi:
                return

            self._push_down(tree_index, tree_lo, tree_hi)
            if arr_lo <= tree_lo <= tree_hi <= arr_hi:
                self._lazy(tree_index, tree_lo, tree_hi, val)
            else:
                mid = (tree_lo+tree_hi) >> 1
                _range_add(2*tree_index+1, tree_lo, mid, arr_lo, arr_hi, val)
                _range_add(2*tree_index+2, mid+1, tree_hi, arr_lo, arr_hi, val)
                self.tree[tree_index] = self.tree[2*tree_index+1] + \
                    self.tree[2*tree_index+2]

        _range_add(0, 0, len(self._arr)-1, arr_lo, arr_hi, val)

    def query(self, arr_lo, arr_hi):
        # hi - inclusive
        def _query(tree_index, tree_lo, tree_hi, arr_lo, arr_hi):
            if arr_hi < tree_lo or arr_lo > tree_hi:
                return

            self._push_down(tree_index, tree_lo, tree_hi)
            if arr_lo <= tree_lo <= tree_hi <= arr_hi:
                print(0, tree_index, self.tree[tree_index])
                return self.tree[tree_index]

            mid = (tree_lo+tree_hi) >> 1
            if arr_lo > mid:
                res = _query(2*tree_index+2, mid+1, tree_hi, arr_lo, arr_hi)
                print(1, tree_index, res)
                return res
            elif arr_hi <= mid:
                res = _query(2*tree_index+1, tree_lo, mid, arr_lo, arr_hi)
                print(2, tree_index, res)
                return res
            else:
                res = _query(2*tree_index+2, mid+1, tree_hi, arr_lo, arr_hi) + \
                    _query(2*tree_index+1, tree_lo, mid, arr_lo, arr_hi)
                print(3, tree_index, res)
                return res

        return _query(0, 0, len(self._arr)-1, arr_lo, arr_hi)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
        range_sum = RangeSumSegmentTree(arr)
        print(range_sum.lazy)
        print(range_sum.tree)
        print('-'*10)
        self.assertEqual(range_sum.query(2, 8), 123)
        range_sum.add(3, 6)
        print(range_sum.lazy)
        print(range_sum.tree)
        print('-'*10)
        self.assertEqual(range_sum.query(2, 8), 129)
        range_sum.range_add(0, 9, 5)
        print(range_sum.tree)
        print(range_sum.lazy)
        self.assertEqual(range_sum.query(2, 8), 164)
        print('-'*10)
        range_sum.range_add(0, 9, 5)
        print(range_sum.tree)
        print(range_sum.lazy)
        print('-'*10)
        self.assertEqual(range_sum.query(2, 8), 199)
        print(range_sum.query(2, 8), 193)
        print(range_sum.tree)
        print(range_sum.lazy)
        print('-'*10)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
