import unittest
from typing import List
from pprint import pprint
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        in_wordList = False

        # prepare
        trans = collections.defaultdict(set)
        for w in wordList:
            if not in_wordList and w == endWord:
                in_wordList = True
            for i in range(len(w)):
                trans[w[:i]+"*"+w[i+1:]].add(w)

        if not in_wordList:
            return []

        def bfs(successors):
            found = False
            q = [beginWord, ]
            visited = {beginWord, }

            while q and not found:
                nxt_q = []
                cur_visited = set()
                for last in q:
                    for i in range(len(last)):
                        for w in trans[last[:i]+"*"+last[i+1:]]:
                            if w in visited or w == last:
                                continue
                            successors[last].add(w)
                            if w not in cur_visited:
                                cur_visited.add(w)
                                if w == endWord:
                                    found = True
                                else:
                                    nxt_q.append(w)
                visited.update(cur_visited)
                q = nxt_q
            return found, successors

        def dfs(path, begin, end, successors, res):
            if begin == end:
                res.append(path[:])
                return res

            if begin not in successors:
                return res

            for w in successors[begin]:
                path.append(w)
                dfs(path, w, end, successors, res)
                path.pop()
            return res

        f, successors = bfs(collections.defaultdict(set))
        if not f:
            return []
        else:
            return dfs([beginWord, ], beginWord, endWord, successors, [])

    def findLadders1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        in_wordList = False

        # prepare
        trans = collections.defaultdict(set)
        for w in wordList:
            if not in_wordList and w == endWord:
                in_wordList = True
            for i in range(len(w)):
                trans[w[:i]+"*"+w[i+1:]].add(w)

        if not in_wordList:
            return []

        # bfs
        found = False
        res = []
        q = [[beginWord, ], ]
        visited = {beginWord, }

        while q and not found:
            print(q)
            nxt_q = []
            cur_visited = set()
            for seq in q:
                last = seq[-1]
                for i in range(len(last)):
                    pat = last[: i]+"*"+last[i+1:]
                    words = trans[pat]
                    for w in words:
                        if w in visited or w == last:
                            continue
                        cur_visited.add(w)
                        if w == endWord:
                            found = True
                            res.append(seq+[w, ])
                        else:
                            nxt_q.append(seq+[w, ])
            visited.update(cur_visited)
            q = nxt_q
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        res = sol.findLadders(beginWord, endWord, wordList)
        expected = [["hit", "hot", "dot", "dog", "cog"],
                    ["hit", "hot", "lot", "log", "cog"]]
        self.assertCountEqual(res, expected)

    # def test_case_2(self):
    #     sol = Solution()
    #     beginWord = "hit"
    #     endWord = "cog"
    #     wordList = ["hot", "dot", "dog", "lot", "log"]
    #     res = sol.findLadders(beginWord, endWord, wordList)
    #     expected = []
    #     self.assertCountEqual(res, expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
