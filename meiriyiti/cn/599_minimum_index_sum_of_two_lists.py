import unittest
from typing import List
from pprint import pprint
import math

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map2 = {w:i for i,w in enumerate(list2)}
        min_index_sum = math.inf
        res = []
        for i, w in enumerate(list1):
            if w in map2:
                index_sum = map2[w] + i
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    res = [w]
                elif index_sum == min_index_sum:
                    res.append(w)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
        list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
        expected = ["Shogun"]
        self.assertCountEqual(sol.findRestaurant(list1, list2), expected)

    def test_case_2(self):
        sol = Solution()
        list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
        list2 = ["KFC","Shogun","Burger King"]
        expected = ["Shogun"]
        self.assertCountEqual(sol.findRestaurant(list1, list2), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
