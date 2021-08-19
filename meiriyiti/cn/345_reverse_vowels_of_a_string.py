import unittest
from typing import List
from pprint import pprint


class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = set("aeiou")
        arr = list(s)
        i, j = 0, len(arr)-1
        while i < j:
            if arr[i].lower() not in VOWELS:
                i += 1
                continue
            if arr[j].lower() not in VOWELS:
                j -= 1
                continue
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i+1, j-1
        return "".join(arr)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "hello"
        expected = "holle"
        self.assertEqual(sol.reverseVowels(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "leetcode"
        expected = "leotcede"
        self.assertEqual(sol.reverseVowels(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
