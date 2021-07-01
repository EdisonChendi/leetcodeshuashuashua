import unittest
from typing import List
from pprint import pprint
from collections import defaultdict


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # only [5, 10, 20] will shows up
        money = defaultdict(int)
        for b in bills:
            if b == 5:
                money[5] += 1
            if b == 10:
                if money[5]:
                    money[5] -= 1
                    money[10] += 1
                else:
                    return False
            if b == 20:
                if money[10] and money[5]:
                    money[10] -= 1
                    money[5] -= 1
                    money[20] += 1
                elif money[5] >= 3:
                    money[5] -= 3
                    money[20] += 1
                else:
                    return False
        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        bills = [5, 5, 5, 10, 20]
        expected = True
        self.assertEqual(sol.lemonadeChange(bills), expected)

    def test_case_2(self):
        sol = Solution()
        bills = [5, 5, 10]
        expected = True
        self.assertEqual(sol.lemonadeChange(bills), expected)

    def test_case_3(self):
        sol = Solution()
        bills = [10, 10]
        expected = False
        self.assertEqual(sol.lemonadeChange(bills), expected)

    def test_case_4(self):
        sol = Solution()
        bills = [5, 5, 10, 10, 20]
        expected = False
        self.assertEqual(sol.lemonadeChange(bills), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
