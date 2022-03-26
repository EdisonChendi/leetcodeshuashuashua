import unittest
from typing import List
from pprint import pprint


MAPPING = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6'
}


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        i = 0
        j = len(num)-1
        while i <= j:
            ni = num[i]
            nj = num[j]
            if ni in MAPPING and MAPPING[ni] == nj:
                i += 1
                j -= 1
            else:
                return False
        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
