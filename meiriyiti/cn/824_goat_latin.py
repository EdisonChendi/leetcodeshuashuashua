import unittest
from typing import List
from pprint import pprint


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        v = {'a', 'e', 'i', 'o', 'u'}
        res = []
        for i, s in enumerate(sentence.split()):
            if s[0].lower() in v:
                res.append("".join([s, "ma", "a"*(i+1)]))
            else:
                res.append("".join([s[1:], s[0], "ma", "a"*(i+1)]))
        return " ".join(res)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        sentence = "I speak Goat Latin"
        expected = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
        self.assertEqual(sol.toGoatLatin(sentence), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
