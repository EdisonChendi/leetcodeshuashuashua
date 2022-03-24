import unittest
from typing import List
from pprint import pprint


class RangeSumSegmentTree:

    def __init__(self, arr) -> None:
        self._arr = arr
        self.tree = [0]*(4*len(self._arr))
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

    def update(self, arr_index, val):

        def _update(val, tree_index, lo, hi, arr_index):
            if lo == hi:
                self._arr[arr_index] = val
                self.tree[tree_index] = val
                return

            mid = (lo+hi) >> 1
            if arr_index <= mid:
                _update(val, 2*tree_index+1, lo, mid, arr_index)
            else:
                _update(val, 2*tree_index+2, mid+1, hi, arr_index)

            self.tree[tree_index] = self.tree[tree_index*2+1] + \
                self.tree[tree_index*2+2]

        _update(val, 0, 0, len(self._arr)-1, arr_index)

    def query(self, arr_lo, arr_hi):
        # hi - inclusive
        def _query(tree_index, tree_lo, tree_hi, arr_lo, arr_hi):
            if arr_hi < tree_lo or arr_lo > tree_hi:
                return

            if arr_lo <= tree_lo <= tree_hi <= arr_hi:
                return self.tree[tree_index]

            mid = (tree_lo+tree_hi) >> 1
            if arr_lo > mid:
                return _query(2*tree_index+2, mid+1, tree_hi, arr_lo, arr_hi)
            elif arr_hi <= mid:
                return _query(2*tree_index+1, tree_lo, mid, arr_lo, arr_hi)
            else:
                return _query(2*tree_index+2, mid+1, tree_hi, arr_lo, arr_hi) + _query(2*tree_index+1, tree_lo, mid, arr_lo, arr_hi)

        return _query(0, 0, len(self._arr)-1, arr_lo, arr_hi)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
        range_sum = RangeSumSegmentTree(arr)
        self.assertEqual(range_sum.query(2, 8), 123)
        range_sum.update(3, 25)
        self.assertEqual(range_sum.query(2, 8), 129)
        range_sum.update(1, 100)
        self.assertEqual(range_sum.query(2, 8), 129)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
