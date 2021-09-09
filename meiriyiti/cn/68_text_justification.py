import unittest
from typing import List
from pprint import pprint


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def padding(arr, l):
            n, spaces = len(arr), maxWidth-l
            if n == 1:
                return arr[0] + " "*spaces
            res = ""
            s, left = divmod(spaces, n-1)
            for i in range(n-1):
                w = arr[i]
                res += w + " "*(s + (left > 0))
                left -= 1
            res += arr[-1]
            return res

        res, cur, l = [], [], 0
        for w in words:
            if len(cur)+len(w)+l <= maxWidth:
                cur.append(w)
                l += len(w)
            else:
                res.append(padding(cur, l))

                cur = [w, ]
                l = len(w)

        res.append(" ".join(cur)+" "*(maxWidth-l-len(cur)+1))

        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        expected = ["This    is    an",
                    "example  of text",
                    "justification.  "
                    ]
        res = sol.fullJustify(words, maxWidth)
        self.assertCountEqual(expected, res)

    def test_case_2(self):
        sol = Solution()
        words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        maxWidth = 16
        expected = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        res = sol.fullJustify(words, maxWidth)
        self.assertCountEqual(expected, res)

        # def test_edge_case_1(self):
        #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
