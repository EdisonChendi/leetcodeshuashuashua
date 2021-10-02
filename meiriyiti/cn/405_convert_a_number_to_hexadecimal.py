import unittest
from typing import List
from pprint import pprint


CONV = "0123456789abcdef"


class Solution:

    def toHex(self, num: int) -> str:
        ans = []
        for _ in range(8):
            ans.append(CONV[num & 0xf])
            num >>= 4
            if not num:
                break
        return "".join(reversed(ans))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = 26
        expected = "1a"
        self.assertEqual(sol.toHex(num), expected)

    def test_case_2(self):
        sol = Solution()
        num = -1
        expected = "ffffffff"
        self.assertEqual(sol.toHex(num), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
