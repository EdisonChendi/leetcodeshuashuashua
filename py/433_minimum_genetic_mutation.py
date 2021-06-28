import unittest
from typing import List
from pprint import pprint


def valid(f, t):
    return 1 == sum(ch1 != ch2 for ch1, ch2 in zip(f, t))


class Solution:
    def minMutation1(self, start: str, end: str, bank: List[str]) -> int:
        count = 0
        q = {start}
        bank = set(bank)-q

        if end not in bank:
            return -1

        while q:
            count += 1
            nxt_q = set()
            for m in q:
                for b in bank:
                    if valid(m, b):
                        if b == end:
                            return count
                        nxt_q.add(b)
                bank -= nxt_q
            q = nxt_q
        return -1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        count = 0
        N = 8
        q = [start]
        bank = set(bank)-{start}
        G = tuple("ACGT")

        if end not in bank:
            return -1

        while q:
            count += 1
            nxt_q = []
            for g in q:
                for i in range(N):
                    for ch in G:
                        g_mutated = g[:i] + ch + g[i+1:]
                        if g_mutated in bank:
                            if g_mutated == end:
                                return count
                            bank.remove(g_mutated)
                            nxt_q.append(g_mutated)
            q = nxt_q
        return -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        start = "AACCGGTT"
        end = "AACCGGTA"
        bank = ["AACCGGTA"]
        expected = 1
        self.assertEqual(sol.minMutation(start, end, bank), expected)

    def test_case_2(self):
        sol = Solution()
        start = "AACCGGTT"
        end = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        expected = 2
        self.assertEqual(sol.minMutation(start, end, bank), expected)

    def test_case_3(self):
        sol = Solution()
        start = "AAAAACCC"
        end = "AACCCCCC"
        bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        expected = 3
        self.assertEqual(sol.minMutation(start, end, bank), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
