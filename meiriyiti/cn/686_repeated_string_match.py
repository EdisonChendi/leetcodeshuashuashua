import unittest
from typing import List
from pprint import pprint

class Solution1:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        la,lb = len(a),len(b)

        def match(i:int) -> int:
            print(i)
            res = 1
            while i < lb:
                res += 1
                ni = min(i+la, lb)
                if b[i:ni] != a[:ni-i]:
                    return -1
                i = ni
            return res

        if la >= lb:
            if a.find(b) >= 0:
                return 1
            elif (a+a).find(b) > 0:
                return 2
            else:
                return -1
        if set(b)-set(a):
            return -1
        if la == 1:
            return lb

        res = []
        for i in range(1, la+1):
            a_suffix = a[la-i:]
            b_prefix = b[:i]
            if a_suffix == b_prefix:
                r = match(i)
                if r != -1:
                    res.append(r)
        return min(res) if res else -1

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        temp_a = a
        while len(a) < len(b):
            a += temp_a
        a += temp_a

        pos = a.find(b)
        if pos == -1:
            return -1
        
        return (pos + len(b) - 1) // len(temp_a) + 1


class TestSolution(unittest.TestCase):

    def test_case_0(self):
        sol = Solution()
        a = "aaaaaaaaaaaaaaaaaaaaaab"
        b = "ba"
        expected = 2
        self.assertEqual(sol.repeatedStringMatch(a, b), expected)

    def test_case_6(self):
        sol = Solution()
        a = "baaabbbaba"
        b = "baaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbaba"
        expected = 10
        self.assertEqual(sol.repeatedStringMatch(a, b), expected)

    def test_case_5(self):
        sol = Solution()
        a = "abab"
        b = "aba"
        expected = 1
        self.assertEqual(sol.repeatedStringMatch(a, b), expected)

    def test_case_1(self):
        sol = Solution()
        a = "abcd"
        b = "cdabcdab"
        expected = 3
        self.assertEqual(sol.repeatedStringMatch(a, b), expected)

    def test_case_2(self):
        sol = Solution()
        a = "a"
        b = "aa"
        expected = 2
        self.assertEqual(sol.repeatedStringMatch(a, b), expected)

    def test_case_3(self):
        sol = Solution()
        a = "a"
        b = "a"
        expected = 1
        self.assertEqual(sol.repeatedStringMatch(a, b), expected)

    def test_case_4(self):
        sol = Solution()
        a = "abc"
        b = "wxyz"
        expected = -1
        self.assertEqual(sol.repeatedStringMatch(a, b), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
