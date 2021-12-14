import unittest
from typing import List
from pprint import pprint
import operator
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        accu, heap = 0, []
        for dur, ddl in sorted(courses, key=operator.itemgetter(1)):
            accu += dur
            heapq.heappush(heap, -dur)
            if accu > ddl:
                accu += heapq.heappop(heap)
        return len(heap)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
        expected = 3
        self.assertEqual(sol.scheduleCourse(courses), expected)

    def test_case_2(self):
        sol = Solution()
        courses = [[1, 2]]
        expected = 1
        self.assertEqual(sol.scheduleCourse(courses), expected)

    def test_case_3(self):
        sol = Solution()
        courses = [[3, 2], [4, 3]]
        expected = 0
        self.assertEqual(sol.scheduleCourse(courses), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
