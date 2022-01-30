import unittest
from typing import List
from pprint import pprint
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = Counter(s1.split()) + Counter(s2.split())
        return [k for k, cnt in counter.items() if cnt == 1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s1 = "this apple is sweet"
        s2 = "this apple is sour"
        expected = ["sweet", "sour"]
        self.assertCountEqual(sol.uncommonFromSentences(s1, s2), expected)

    def test_case_2(self):
        sol = Solution()
        s1 = "apple apple"
        s2 = "banana"
        expected = ["banana"]
        self.assertCountEqual(sol.uncommonFromSentences(s1, s2), expected)

    def test_case_3(self):
        sol = Solution()
        s1 = "s z z z s"
        s2 = "s z ejt"
        expected = ["ejt"]
        self.assertCountEqual(sol.uncommonFromSentences(s1, s2), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
