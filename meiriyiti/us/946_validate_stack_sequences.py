from re import S
import unittest
from typing import List
from pprint import pprint

class Solution1:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # just by simulation
        stack = []
        lpush, lpop = len(pushed), len(popped)
        i = j = 0
        while (i < lpush or stack) and j < lpop:
            if not stack or stack[-1] != popped[j]:
                if i < len(pushed):
                    stack.append(pushed[i])
                    i += 1
                else:
                    return False
            else:
                stack.pop()
                j += 1
        return i == lpush and j == lpop

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # just by simulation
        stack = []
        i = 0
        for n in pushed:
            stack.append(n)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pushed = [1,2,3,4,5]
        popped = [4,5,3,2,1]
        expected = True
        self.assertEqual(sol.validateStackSequences(pushed, popped), expected)

    def test_case_2(self):
        sol = Solution()
        pushed = [1,2,3,4,5]
        popped = [4,3,5,1,2]
        expected = False
        self.assertEqual(sol.validateStackSequences(pushed, popped), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
