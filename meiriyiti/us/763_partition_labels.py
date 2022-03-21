import unittest
from typing import List
from pprint import pprint

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {ch:i for i,ch in enumerate(s)}

        i = 0
        last = -1
        right = -1
        res = [-1,]
        for i,ch in enumerate(s):
            right = max(right, last_pos[ch])
            if i == right:
                res.append(i-last)
                last = i
        return res[1:]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "ababcbacadefegdehijhklij"
        expected = [9,7,8]
        self.assertEqual(sol.partitionLabels(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "eccbbbbdec"
        expected = [10]
        self.assertEqual(sol.partitionLabels(s), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
