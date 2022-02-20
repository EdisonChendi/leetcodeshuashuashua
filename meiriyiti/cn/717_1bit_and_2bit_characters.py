import unittest
from typing import List
from pprint import pprint


class Solution1:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        def helper(bits: List[int], i: int) -> bool:
            if i == len(bits):
                return True

            if i == len(bits) - 1:
                return bits[i] == 0

            if bits[i] == 0 and helper(bits, i+1):
                return True

            next_two = bits[i:i+2]
            if (next_two == [1, 0] or next_two == [1, 1]) and helper(bits, i+2):
                return True

            return False

        return helper(bits[:-1], 0)


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        N, i = len(bits), 0
        while i < N-1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == N-1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        bits = [1, 0, 0]
        expected = True
        self.assertEqual(sol.isOneBitCharacter(bits), expected)

    def test_case_2(self):
        sol = Solution()
        bits = [1, 1, 1, 0]
        expected = False
        self.assertEqual(sol.isOneBitCharacter(bits), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
