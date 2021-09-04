import unittest
from typing import List
from pprint import pprint


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def walk(pos, c, x, y):
            for _ in range(c):
                npos = (pos[0]+x, pos[1]+y)
                if npos in obstacles:
                    break
                pos = npos
            return pos

        def dis(p):
            return p[0]**2 + p[1]**2

        obstacles = set(tuple(o) for o in obstacles)
        x, y = 0, 1
        pos = (0, 0)
        res = 0
        for c in commands:
            if c == -1:
                x, y = y, -x
            elif c == -2:
                x, y = -y, x
            else:
                pos = walk(pos, c, x, y)
                res = max(res, dis(pos))
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        commands = [4, -1, 3]
        obstacles = []
        res = 25
        self.assertEqual(sol.robotSim(commands, obstacles), res)

    def test_case_2(self):
        sol = Solution()
        commands = [4, -1, 4, -2, 4]
        obstacles = [[2, 4]]
        res = 65
        self.assertEqual(sol.robotSim(commands, obstacles), res)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
