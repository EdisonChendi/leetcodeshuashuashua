import unittest
from typing import List
from pprint import pprint
from collections import Counter

class Solution1:
    # LTE
    def originalDigits(self, s: str) -> str:
        # backtracking
        NUMBERS = {
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }.items()
        def try_match(counter, eng):
            eng_counter = Counter(eng)
            for ch, cnt in eng_counter.items():
                if not (ch in counter and counter[ch]>=cnt):
                    return False
            counter -= eng_counter
            return True

        def backtrack(counter, res):
            if len(counter) == 0:
                return True
            for eng, n in NUMBERS:
                if try_match(counter, eng):
                    res.append(n)
                    if backtrack(counter, res):
                        return True
                    res.pop()
                    counter += Counter(eng)
        res = []
        backtrack(Counter(s), res)
        return "".join(map(str, res))

"""
"zero": "0",
"one": "1",
"two": "2",
"three": "3",
"four": "4",
"five": "5",
"six": "6",
"seven": "7",
"eight": "8",
"nine": "9"
-------------------
e: 0 1 3 5 7 8 9
o: 0 1 2 4
r: 0 3 4
z: 0
n: 1 7 9
t: 2 3 8
w: 2
h: 3 8
f: 4 5
u: 4
i: 5 6 8 9
v: 5 7
s: 6 7
x: 6
g: 8
"""
class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)
        res = [0]*10
        res[0] = cnt['z']
        res[2] = cnt['w']
        res[4] = cnt['u']
        res[6] = cnt['x']
        res[8] = cnt['g']

        res[3] = cnt['h'] - res[8]
        res[5] = cnt['f'] - res[4]
        res[7] = cnt['v'] - res[5]

        res[1] = cnt['o'] - res[0] - res[2] - res[4]
        res[9] = (cnt['n'] - res[1] - res[7])//2

        return "".join((str(i)*res[i]) for i in range(10))

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "owoztneoer"
        expected = "012"
        self.assertEqual(sol.originalDigits(s), expected)
        
    def test_case_2(self):
        sol = Solution()
        s = "fviefuro"
        expected = "45"
        self.assertEqual(sol.originalDigits(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
