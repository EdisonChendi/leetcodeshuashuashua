import unittest
from typing import List
from pprint import pprint


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        prime = 31
        mod = 2**63 - 1
        h = [0]*(1+len(s))
        for i in range(len(s)):
            h[i+1] = (prime*h[i] + ord(s[i])-ord('a')) % mod

        def rk_check(l: int) -> int:
            hash = h[l]
            seen = {hash}
            power = prime**l % mod

            for i in range(l, len(s)):
                hash = (hash*prime + ord(s[i])-ord('a') -
                        power*(ord(s[i-l])-ord('a'))) % mod
                if hash in seen:
                    return i-l+1
                seen.add(hash)
            return -1

        l, r = 0, len(s)
        start, llen = -1, 0
        while l <= r:
            mid = (l+r) >> 1
            found = rk_check(mid)
            if found != -1:
                start = found
                llen = mid
                l = mid + 1
            else:
                r = mid - 1
        return s[start:start+llen] if start != -1 else ""


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "banana"
        expected = "ana"
        self.assertEqual(sol.longestDupSubstring(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "abcd"
        expected = ""
        self.assertEqual(sol.longestDupSubstring(s), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
