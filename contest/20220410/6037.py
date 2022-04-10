import unittest
from typing import List
from pprint import pprint


class Solution:
    def largestInteger(self, num: int) -> int:
        NUM = num
        even = []
        odd = []
        while num > 0:
            num, rem = divmod(num, 10)
            if rem % 2 == 0:
                even.append(rem)
            else:
                odd.append(rem)
        even.sort()
        odd.sort()
        res = 0
        i = j = k = 0
        num = NUM
        while num > 0:
            num, rem = divmod(num, 10)
            if rem % 2 == 0:
                res += even[i] * (10**k)
                i += 1
            else:
                res += odd[j] * (10**k)
                j += 1
            k += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = 1234
        expected = 3412
        self.assertEqual(sol.largestInteger(num), expected)

    def test_case_2(self):
        sol = Solution()
        num = 65875
        expected = 87655
        self.assertEqual(sol.largestInteger(num), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
