import unittest
from typing import List
from pprint import pprint


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        q = []
        j = 0
        for i in reversed(range(len(s))):
            if s[i] != '-':
                if j == k:
                    j = 0
                    q.append('-')
                j += 1
                q.append(s[i].upper())
        return "".join(reversed(q))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "5F3Z-2e-9-w"
        k = 4
        expected = "5F3Z-2E9W"
        self.assertEqual(sol.licenseKeyFormatting(s, k), expected)

    def test_case_2(self):
        sol = Solution()
        s = "2-5G-3-J"
        k = 2
        expected = "2-5G-3J"
        self.assertEqual(sol.licenseKeyFormatting(s, k), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
