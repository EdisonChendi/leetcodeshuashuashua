import unittest
from typing import List
from pprint import pprint


class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for i in range(min(map(len, strs))):
            cur = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != cur:
                    return "".join(res)
            res.append(cur)
        return "".join(res)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for chs in zip(*strs):
            if len(set(chs)) != 1:
                break
            res.append(chs[0])
        return "".join(res)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        self.assertEqual(sol.longestCommonPrefix(strs), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
