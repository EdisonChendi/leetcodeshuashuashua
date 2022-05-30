import unittest
from typing import List
from pprint import pprint

class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.min = [0]*4*n
        self.sum = [0]*4*n

    def add(self, i, l, r, idx, val):
        if idx < l or idx > r:
            return

        if l == r:
            self.min[i] += val
            self.sum[i] += val
            return

        m = l+r >> 1
        if idx <= m:
            self.add(2*i, l, m, idx, val)
        else:
            self.add(2*i+1, m+1, r, idx, val)
        self.min[i] = min(self.min[2*i], self.min[2*i+1])
        self.sum[i] = self.sum[2*i] + self.sum[2*i+1]

    
    def query_range_sum(self, i, l, r, L, R):
        if R < l or L > r:
            return 0
        if L <= l <= r <= R:
            return self.sum[i]
        m = l+r >> 1
        return self.query_range_sum(2*i, l, m, L, R) + self.query_range_sum(2*i+1, m+1, r, L, R)

    def row(self, i):
        return self.query_range_sum(1, 1, self.n, i, i)

    def index(self, i, l, r, R, val): # 返回[1, R]中最小一排座位数<=val的
        if self.min[i] > val: return 0

        if l == r: return l

        m = (l+r) >> 1

        if self.min[2*i] <= val:
            return self.index(2*i, l, m, R, val)

        if R > m:
            return self.index(2*i+1, m+1, r, R, val)

        return 0

    def gather(self, k: int, maxRow: int) -> List[int]:
        idx = self.index(1, 1, self.n, maxRow+1, self.m-k)
        if idx == 0:
            return []
        seats = self.row(idx)
        self.add(1, 1, self.n, idx, k)
        return [idx-1, seats]

    def scatter(self, k: int, maxRow: int) -> bool:
        total = self.m*(maxRow+1) - self.query_range_sum(1, 1, self.n, 1, maxRow+1)
        if total < k:
            return False
        i = self.index(1, 1, self.n, maxRow+1, self.m-1) # 第一排未满的
        while True:
            seats = self.m - self.query_range_sum(1, 1, self.n, i, i)
            if k <= seats:
                self.add(1, 1, self.n, i, k)
                return True
            self.add(1, 1, self.n, i, seats)
            k -= seats
            i += 1


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        # ["BookMyShow", "gather", "gather", "scatter", "scatter"]
        # [[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
        show = BookMyShow(2, 5)
        # [null, [0, 0], [], true, false]
        print(show.gather(4, 0)) # [0, 0]
        print(show.gather(2, 0)) # []
        print(show.scatter(5, 1)) # true
        print(show.scatter(5, 1)) # false
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
