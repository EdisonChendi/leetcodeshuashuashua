import unittest
from typing import List
from pprint import pprint

import collections
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        low = upp = dig = 0
        repeat = collections.Counter()
        N = len(password)

        accu = 0
        one = 0
        two = 0
        for i, ch in enumerate(password):
            if i > 0:
                if ch != password[i-1]:
                    if accu >= 3:
                        repeat[accu] += 1
                        if accu % 3 == 0: one += 1
                        elif accu % 3 == 1: two += 1
                    accu = 1
                else: accu += 1
            else: accu += 1

            low += ch.islower() 
            upp += ch.isupper()
            dig += ch.isdigit()
        else:
            if accu >= 3:
                repeat[accu] += 1
                if accu % 3 == 0: one += 1
                elif accu % 3 == 1: two += 1
        
        low = max(0, 1-low)
        upp = max(0, 1-upp)
        dig = max(0, 1-dig)
        missing = low + upp + dig
        
        # change to break the repeating
        change = sum(n * (i//3) for i, n in repeat.items())
        # print(repeat)
        # print(missing, change)
        
        if N < 6:
            # always insert
            return max(6-N, missing)
        elif 6 <= N <= 20:
            # always replace
            return max(change, missing)
        else:
            # must do delete
            delete = N - 20

            # then do change
            # but some delete can be used to reduce change
            change -= min(delete, one)
            change -= min(max(delete-one, 0), 2*two)//2
            change -= max(delete-one-2*two, 0)//3

            return delete + max(missing, change)



class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        password = "a"
        expected = 5
        self.assertEqual(sol.strongPasswordChecker(password), expected)

    def test_case_2(self):
        sol = Solution()
        password = "aA1"
        expected = 3
        self.assertEqual(sol.strongPasswordChecker(password), expected)

    def test_case_3(self):
        sol = Solution()
        password = "1337C0d3"
        expected = 0
        self.assertEqual(sol.strongPasswordChecker(password), expected)
        
    def test_case_4(self):
        sol = Solution()
        password = "aaa111"
        expected = 2
        self.assertEqual(sol.strongPasswordChecker(password), expected)
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
