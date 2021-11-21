import unittest
from typing import List
from pprint import pprint


def lowbit(n):
    return n & (-n)


# aka. Wenwick Tree
class BinaryIndexTree:

    def __init__(self, arr):
        self._origial_arr = arr
        self.arr = [0, ]*(len(self._origial_arr)+1)
        for i, v in enumerate(self._origial_arr):
            self.inc(i+1, v)

    def inc(self, i, v):
        self._origial_arr[i-1] = v
        while i < len(self.arr):
            self.arr[i] += v
            i += lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.arr[i]
            i -= lowbit(i)
        return res

    def query_range(self, i, j):
        return self.query(j) - self.query(i-1)


class TestSolution(unittest.TestCase):

    def test_case_query_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        tree = BinaryIndexTree(arr)
        self.assertEqual(tree.query(10), sum(arr[:10]))
        self.assertEqual(tree.query(3), sum(arr[:3]))

    def test_case_query_range_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        tree = BinaryIndexTree(arr)
        self.assertEqual(tree.query_range(2, 5), sum(arr[1:5]))
        self.assertEqual(tree.query_range(4, 5), 9)

    def test_case_update_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        tree = BinaryIndexTree(arr)
        tree.inc(2, -3)
        self.assertEqual(tree.query(10), 52)
        self.assertEqual(tree.query(3), 3)
        self.assertEqual(tree.query_range(2, 5), 11)
        self.assertEqual(tree.query_range(4, 5), 9)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
