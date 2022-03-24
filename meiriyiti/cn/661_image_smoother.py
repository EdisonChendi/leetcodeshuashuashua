import unittest
from typing import List
from pprint import pprint

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        H,W = len(img), len(img[0])
        def get(i,j):
            if 0 <= i < H and 0 <= j < W:
                return img[i][j],1
            else:
                return 0,0

        DIRs = ((0,1),(0,-1),(1,0),(-1,0),(0,0),(1,1),(-1,1),(1,-1),(-1,-1)) 
        def smooth(i,j):
            count = s = 0
            for di,dj in DIRs:
                v, c = get(i+di, j+dj)
                s += v
                count += c
            return s // count

        res = [[0]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                res[i][j] = smooth(i,j)
        return res

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        img = [[100,200,100],[200,50,200],[100,200,100]]
        expected = [[137,141,137],[141,138,141],[137,141,137]]
        self.assertCountEqual(sol.imageSmoother(img), expected)
        
    def test_case_2(self):
        sol = Solution()
        img = [[1,1,1],[1,0,1],[1,1,1]]
        expected = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertCountEqual(sol.imageSmoother(img), expected)
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
