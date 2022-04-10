import unittest
from typing import List
from pprint import pprint

TABLE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
         "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        seen = set()
        for w in words:
            morse = "".join([TABLE[ord(ch)-ord('a')] for ch in w])
            seen.add(morse)
        return len(seen)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        words = ["gin", "zen", "gig", "msg"]
        expected = 2
        self.assertEqual(sol.uniqueMorseRepresentations(words), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
