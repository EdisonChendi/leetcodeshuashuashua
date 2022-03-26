import unittest
from typing import List
from pprint import pprint


class Solution1:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        def prefix(i, word):
            if len(word) > len(s)-i:
                return False
            j = 0
            while j < len(word):
                if s[i] != word[j]:
                    return False
                i += 1
                j += 1
            return True

        def merge(bounds, cur):
            if not bounds:
                bounds.append(cur)
            else:
                last = bounds.pop()
                if last[1] < cur[0]-1:
                    bounds.append(last)
                    bounds.append(cur)
                else:
                    bounds.append([last[0], max(last[1], cur[1])])

        bounds = []
        for i in range(len(s)):
            for w in words:
                if prefix(i, w):
                    bound = [i, i+len(w)-1]
                    merge(bounds, bound)

        if not bounds:
            return s
        else:
            res = []
            if bounds[0][0] > 0:
                res.append(s[:bounds[0][0]])

            for b1, b2 in zip(bounds, (bounds[1:]+[[len(s), None]])):
                res.append(f"<b>{s[b1[0]:b1[1]+1]}</b>")
                res.append(f"{s[b1[1]+1:b2[0]]}")

            return "".join(res)


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:

        N = len(s)
        bold = [False]*N
        end = -1
        for i in range(len(s)):
            for w in words:
                if s.startswith(w, i):
                    end = max(end, i+len(w)-1)
            bold[i] = end >= i
        i = 0
        res = []
        while i < N:
            if not bold[i]:
                res.append(s[i])
                i += 1
            else:
                res.append("<b>")
                while i < N and bold[i]:
                    res.append(s[i])
                    i += 1
                res.append("</b>")

        return "".join(res)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "abcxyz123"
        words = ["abc", "123"]
        expected = "<b>abc</b>xyz<b>123</b>"
        self.assertEqual(sol.addBoldTag(s, words), expected)

    def test_case_2(self):
        sol = Solution()
        s = "aaabbcc"
        words = ["aaa", "aab", "bc"]
        expected = "<b>aaabbc</b>c"
        self.assertEqual(sol.addBoldTag(s, words), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
