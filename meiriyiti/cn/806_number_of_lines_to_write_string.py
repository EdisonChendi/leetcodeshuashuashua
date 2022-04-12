import unittest
from typing import List
from pprint import pprint


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        length = 0
        ORD_A = ord('a')
        for ch in s:
            l = widths[ord(ch)-ORD_A]
            length += l
            if length > 100:
                lines += 1
                length = l
        return [lines, length]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                  10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        s = "abcdefghijklmnopqrstuvwxyz"
        expected = [3, 60]
        self.assertListEqual(sol.numberOfLines(widths, s), expected)

    def test_case_2(self):
        sol = Solution()
        widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                  10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        s = "bbbcccdddaaa"
        expected = [2, 4]
        self.assertListEqual(sol.numberOfLines(widths, s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
