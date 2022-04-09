import heapq
import unittest
from typing import List
from pprint import pprint


class Solution1:
    # TLE
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        def dist(x1, y1, x2, y2):
            return abs(x1-x2) + abs(y1-y2)

        if sx > tx or sy > ty:
            return False
        # A* search
        h = [(dist(sx, sy, tx, ty), sx, sy)]
        visited = {(sx, sy)}
        while h:
            _, x, y = heapq.heappop(h)
            if x == tx and y == ty:
                return True
            if x+y <= ty and (x, x+y) not in visited:
                visited.add((x, x+y))
                heapq.heappush(h, (dist(x, x+y, tx, ty), x, x+y))
            if x+y <= tx and (x+y, y) not in visited:
                visited.add((x+y, y))
                heapq.heappush(h, (dist(x+y, x, tx, ty), x+y, y))
        return False


class Solution2:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # still TLE - but pass more tests than the A* approach
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                tx = tx-ty
            else:
                ty = ty-tx
        return False


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            tx, ty = tx % ty, ty % tx
        else:
            return tx == sx and ty >= sy and (ty-sy) % tx == 0 or \
                ty == sy and tx >= sx and (tx-sx) % ty == 0


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        sol = Solution()
        sx = 6
        sy = 5
        tx = 11
        ty = 16
        expected = True
        self.assertEqual(sol.reachingPoints(sx, sy, tx, ty), expected)

    def test_case_1(self):
        sol = Solution()
        sx = 1
        sy = 1
        tx = 3
        ty = 5
        expected = True
        self.assertEqual(sol.reachingPoints(sx, sy, tx, ty), expected)

    def test_case_2(self):
        sol = Solution()
        sx = 1
        sy = 1
        tx = 2
        ty = 2
        expected = False
        self.assertEqual(sol.reachingPoints(sx, sy, tx, ty), expected)

    def test_case_3(self):
        sol = Solution()
        sx = 1
        sy = 1
        tx = 1
        ty = 1
        expected = True
        self.assertEqual(sol.reachingPoints(sx, sy, tx, ty), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
