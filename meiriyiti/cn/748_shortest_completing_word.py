import unittest
from typing import List
from pprint import pprint
import collections

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_counter = collections.Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        return min((w for w in words if not (license_counter-collections.Counter(w))), key=len)



class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        licensePlate = "iMSlpe4"
        words = ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]
        expected = "simple"
        self.assertEqual(sol.shortestCompletingWord(licensePlate, words), expected)
        
    def test_case_2(self):
        sol = Solution()
        licensePlate = "OgEu755"
        words = ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]
        expected = "enough"
        self.assertEqual(sol.shortestCompletingWord(licensePlate, words), expected)
        
    def test_case_3(self):
        sol = Solution()
        licensePlate = "1s3 PSt"
        words = ["step","steps","stripe","stepple"]
        expected = "steps"
        self.assertEqual(sol.shortestCompletingWord(licensePlate, words), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
