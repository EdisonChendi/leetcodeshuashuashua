import unittest
from typing import List
from pprint import pprint

"""
n people standing in a circle
1 people is killed very other k people
begin at index 0
eg: n = 7, k = 3

round 0:
0 1 2 3 4 5 6 7
    x      
0 1 3 4 5 6 7
        x  
0 1 3 4 6 7
x          
1 3 4 6 7
    x          
1 3 6 7
x             
3 6 7
    x            
3 6
x
6
-> 6
"""


class Solution1:
    """
    recursive
    """

    def josephus(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        return (self.josephus(n-1, k)+k) % n


class Solution:
    """
    iterative
    """

    def josephus(self, n: int, k: int) -> int:
        res = 0

        for i in range(2, n+1):
            res = (res + k) % i

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 8
        k = 3
        expected = 6
        self.assertEqual(sol.josephus(n, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
