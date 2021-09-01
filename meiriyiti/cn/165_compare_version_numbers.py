import unittest
from typing import List
from pprint import pprint
from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(version1.split("."), version2.split("."), fillvalue=0):
            x,y = int(v1),int(v2)
            if x != y:
                return 1 if x > y else -1
        return 0

    def compareVersion1(self, version1: str, version2: str) -> int:
        V1, V2 = version1.split("."), version2.split(".")
        i,j,N1,N2 = 0,0,len(V1),len(V2)
        while i < N1 and j < N2:
            v1, v2 = int(V1[i]), int(V2[j])
            if v1 != v2:
                return 1 if v1 > v2 else -1
            i, j = i+1, j+1
        if N1 == N2:
            return 0
        if i < N1:
            return int(any(int(V1[p])!=0 for p in range(i, N1)))
        else:
            return -int(any(int(V2[p])!=0 for p in range(j, N2)))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        version1 = "1.01"; version2 = "1.001"
        expected = 0
        self.assertEqual(sol.compareVersion(version1, version2), expected)
        
    def test_case_2(self):
        sol = Solution()
        version1 = "1.0"; version2 = "1.0.0"
        expected = 0
        self.assertEqual(sol.compareVersion(version1, version2), expected)

    def test_case_3(self):
        sol = Solution()
        version1 = "0.1"; version2 = "1.1"
        expected = -1
        self.assertEqual(sol.compareVersion(version1, version2), expected)

    def test_case_4(self):
        sol = Solution()
        version1 = "1.0.1"; version2 = "1"
        expected = 1
        self.assertEqual(sol.compareVersion(version1, version2), expected)

    def test_case_5(self):
        sol = Solution()
        version1 = "7.5.2.4"; version2 = "7.5.3"
        expected = -1
        self.assertEqual(sol.compareVersion(version1, version2), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
