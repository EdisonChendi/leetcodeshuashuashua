import unittest
from typing import List
from pprint import pprint


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j, res = 0, len(people)-1, 0
        while i < j:
            res += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return (res+1) if i == j else res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        people = [1, 2]
        limit = 3
        expected = 1
        self.assertEqual(sol.numRescueBoats(people, limit), expected)

    def test_case_2(self):
        sol = Solution()
        people = [3, 2, 2, 1]
        limit = 3
        expected = 3
        self.assertEqual(sol.numRescueBoats(people, limit), expected)

    def test_case_3(self):
        sol = Solution()
        people = [3, 5, 3, 4]
        limit = 5
        expected = 4
        self.assertEqual(sol.numRescueBoats(people, limit), expected)

    def test_case_4(self):
        sol = Solution()
        people = [2, 4]
        limit = 5
        expected = 2
        self.assertEqual(sol.numRescueBoats(people, limit), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
