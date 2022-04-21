from distutils.command.clean import clean
from turtle import back
import unittest
from typing import List
from pprint import pprint


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        cleaned = set()
        # right -> [(-1,0), (0,1), (1,0), (0,-1)] -> x,y = y,-x
        # left -> [(-1,0),(0,-1),(1,0),(0,1)] -> x,y = -y, x

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(i, j, ni, nj):
            # move forward
            cleaned.add((i, j))
            robot.clean()

            for _ in range(4):
                if (i+ni, j+nj) not in cleaned and robot.move():
                    backtrack(i+ni, j+nj, ni, nj)
                    go_back()
                robot.turnRight()
                ni, nj = nj, -ni

        backtrack(0, 0, -1, 0)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
