import unittest
from typing import List
from pprint import pprint

def int2bin(n):
    assert 0 <= n <= 255
    bin_repr = bin(n)[2:]
    return "0"*(8-len(bin_repr)) + bin_repr


class Solution1:
    def validUtf8(self, data: List[int]) -> bool:
        N = len(data)
        i = 0
        while i < N:
            bin_repr = int2bin(data[i])
            if bin_repr[0] == "0":
                i += 1
                continue

            if bin_repr[0:3] == "110":
                cnt = 1
            elif bin_repr[0:4] == "1110":
                cnt = 2
            elif bin_repr[0:5] == "11110":
                cnt = 3
            else:
                return False
            
            if i+cnt+1 > N:
                return False
            
            for j in range(i+1, i+cnt+1):
                if not int2bin(data[j]).startswith("10"):
                    return False
            i += cnt+1
        return True

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        N = len(data)
        i = 0
        while i < N:
            n = data[i]
            if n >> 7 == 0:
                i += 1
                continue
            if n >> 5 == 6:
                cnt = 1
            elif n >> 4 == 14:
                cnt = 2
            elif n >> 3 == 30:
                cnt = 3
            else:
                return False
            
            if i+cnt+1 > N:
                return False
            
            for j in range(i+1, i+cnt+1):
                if data[j] >> 6 != 2:
                    return False
            i += cnt+1

        return True

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        data = [197,130,1]
        expected = True
        self.assertEqual(sol.validUtf8(data), expected)

    def test_case_2(self):
        sol = Solution()
        data = [235,140,4]
        expected = False
        self.assertEqual(sol.validUtf8(data), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
