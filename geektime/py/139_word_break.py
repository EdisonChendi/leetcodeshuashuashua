import unittest
from typing import List
from pprint import pprint

# 递推公式, DP - 截止到i是否可以拼出来
# DP[i] = 任何i之前的可以拼出来的 + 截取字符串s[j,i] 是在wordDict里面的
# 否则s截止到i是拼不出来的

class Solution:
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:

        cache = {}

        def sub(s):
            if s == "":
                return True
            if s in cache:
                return cache[s]

            res = any(sub(s[len(w):]) for w in wordDict if s.startswith(w))
            cache[s] = res
            return res

        return sub(s)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # initialize
        dp = [True]+[False, ]*len(s)
        words = set(wordDict)

        for i in range(len(s)):
            dp[i+1] = any(s[j:i+1] in words for j in range(i+1) if dp[j])
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "leetcode"
        wordDict = ["leet", "code"]
        expected = True
        self.assertEqual(sol.wordBreak(s, wordDict), expected)

    def test_case_2(self):
        sol = Solution()
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        expected = True
        self.assertEqual(sol.wordBreak(s, wordDict), expected)

    def test_case_3(self):
        sol = Solution()
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        expected = False
        self.assertEqual(sol.wordBreak(s, wordDict), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
