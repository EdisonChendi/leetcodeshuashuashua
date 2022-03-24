import unittest
from typing import List
from pprint import pprint

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        i = 0
        j = len(people)-1
        people.sort()
        while i < j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            ans += 1
        return ans + (i==j)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        people = [1,2]
        limit = 3
        expected = 1
        self.assertEqual(sol.numRescueBoats(people, limit), expected)

    def test_case_2(self):
        sol = Solution()
        people = [3,2,2,1]
        limit = 3
        expected = 3
        self.assertEqual(sol.numRescueBoats(people, limit), expected)
        
    def test_case_3(self):
        sol = Solution()
        people = [3,5,3,4]
        limit = 5
        expected = 4
        self.assertEqual(sol.numRescueBoats(people, limit), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
