import unittest
from typing import List
from pprint import pprint

def check(radius, houses, heaters):
    i,j = 0,0
    while j < len(houses):
        h = houses[j]
        if heaters[i] - radius <= h <= heaters[i] + radius:
            j += 1
        elif h > heaters[i]+radius:
            if i+1 < len(heaters):
                i += 1
            else:
                return False
        else:
            return False
    return True

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # binary search
        houses.sort()
        heaters.sort()

        l,r = 0, houses[-1]+heaters[-1]
        while l < r:
            mid = (l+r)//2
            if check(mid, houses, heaters):
                r = mid
            else:
                l = mid+1
        return r

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        houses = [1,2,3]; heaters = [2]
        expected = 1
        self.assertEqual(sol.findRadius(houses, heaters), expected)

    def test_case_2(self):
        sol = Solution()
        houses = [1,2,3,4]; heaters = [1,4]
        expected = 1
        self.assertEqual(sol.findRadius(houses, heaters), expected)

    def test_case_3(self):
        sol = Solution()
        houses = [1,5]; heaters = [2]
        expected = 3
        self.assertEqual(sol.findRadius(houses, heaters), expected)
        
    def test_case_4(self):
        sol = Solution()
        houses = [1]
        heaters = [1,2,3,4]
        expected = 0
        self.assertEqual(sol.findRadius(houses, heaters), expected)

    def test_case_5(self):
        sol = Solution()
        houses = [1,2,3,5,15]
        heaters = [2,30]
        expected = 13
        self.assertEqual(sol.findRadius(houses, heaters), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
