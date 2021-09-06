import unittest
from typing import List
from pprint import pprint


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        N = 4
        start = '0000'
        q = [start, ]
        visited = {start, }
        count = 0

        while q:
            new_q = []
            while q:
                lock = q.pop()
                if lock in deadends:
                    continue

                if lock == target:
                    return count

                for i in range(N):
                    wheel = int(lock[i])

                    up = (wheel+1) if wheel != 9 else 0
                    lock_up = lock[:i]+str(up)+lock[i+1:]
                    if lock_up not in visited:
                        visited.add(lock_up)
                        new_q.append(lock_up)

                    down = (wheel-1) if wheel != 0 else 9
                    lock_down = lock[:i]+str(down)+lock[i+1:]
                    if lock_down not in visited:
                        visited.add(lock_down)
                        new_q.append(lock_down)

            count += 1
            q = new_q

        return -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        deadends = ["0201", "0101", "0102", "1212", "2002"]
        target = "0202"
        expected = 6
        self.assertEqual(sol.openLock(deadends, target), expected)

    def test_case_2(self):
        sol = Solution()
        deadends = ["8888"]
        target = "0009"
        expected = 1
        self.assertEqual(sol.openLock(deadends, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
