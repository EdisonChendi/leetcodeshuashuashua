import unittest
from typing import List
from pprint import pprint
import collections
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L,N = 10,len(s)
        bin = {'A': 0, 'C':1, "G":2, "T":3}
        counter = collections.defaultdict(int)

        if N <= L:
            return []
        window = 0
        for i in range(L):
            window = (window << 2) | bin[s[i]]
        counter[window] += 1
        MASK = (1 << L*2) - 1
        res = []
        for i in range(1, N-L+1):
            window = ((window<<2) | bin[s[i+L-1]]) & MASK
            counter[window] += 1
            if counter[window] == 2:
                res.append(s[i:i+L])
        return res
        

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        expected = ["AAAAACCCCC","CCCCCAAAAA"]
        self.assertCountEqual(sol.findRepeatedDnaSequences(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "AAAAAAAAAAAAA"
        expected = ["AAAAAAAAAA"]
        self.assertCountEqual(sol.findRepeatedDnaSequences(s), expected)
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
