from tracemalloc import start
import unittest
from typing import List
from pprint import pprint

def parse(log):
    fid, event, time = log.split(':')
    return int(fid), 0 if event == "start" else 1, int(time)

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0]*n
        stack = []
        for log in logs:
            fid, event, time = parse(log)
            if event == 0:
                stack.append((fid, event, time))
            else:
                cur = 0
                while stack[-1][1] == 2:
                    cur += stack.pop()[2]
                _, _, start_time = stack.pop()
                elapsed_time = time-start_time+1
                res[fid] += elapsed_time - cur
                stack.append((fid, 2, elapsed_time))
        return res

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 2
        logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
        expected = [3,4]
        self.assertListEqual(sol.exclusiveTime(n, logs), expected)
        
    def test_case_2(self):
        sol = Solution()
        n = 1
        logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
        expected = [8]
        self.assertListEqual(sol.exclusiveTime(n, logs), expected)

    def test_case_3(self):
        sol = Solution()
        n = 2
        logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
        expected =  [7,1]
        self.assertListEqual(sol.exclusiveTime(n, logs), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
