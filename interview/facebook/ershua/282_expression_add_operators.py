import unittest
from typing import List
from pprint import pprint

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        L = len(num)
        def backtrack(idx,prv,accu,cur):
            if idx == L:
                if accu == target:
                    res.append(cur)
                return
            n = 0
            for i in range(idx, L):
                if i > idx and num[idx] == '0':
                    break
                n = n*10 + int(num[i])
                if idx == 0:
                    backtrack(i+1, n, n, num[idx:i+1])
                else:
                    backtrack(i+1, n, accu+n, cur+"+"+num[idx:i+1])
                    backtrack(i+1, -n, accu-n, cur+"-"+num[idx:i+1])
                    backtrack(i+1, n*prv, accu-prv+n*prv, cur+"*"+num[idx:i+1])

        backtrack(0, 0, 0, "")
        return res

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = "123"
        target= 6
        expected = ["1*2*3","1+2+3"]
        self.assertCountEqual(sol.addOperators(num, target), expected)

    def test_case_2(self):
        sol = Solution()
        num = "232"
        target= 8
        expected = ["2*3+2","2+3*2"]
        self.assertCountEqual(sol.addOperators(num, target), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
