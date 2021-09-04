import unittest
from typing import List
from pprint import pprint


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        GENE_LEN = 8
        CHOICES = ('A','C','G','T')
        front, back = {start}, {end}
        bank.discard(front)
        bank.discard(end)
        dist = 0
        while front:
            new_front = set()
            dist += 1
            for gene in front:
                for choice in CHOICES:
                    for i in range(GENE_LEN):
                        new_gene = gene[:i]+choice+gene[i+1:]
                        if new_gene in back:
                            return dist
                        if new_gene in bank:
                            bank.discard(new_gene)
                            new_front.add(new_gene)
            front = new_front
            if len(front) > len(back):
                front, back = back, front
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
        bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        expected = 2
        self.assertEqual(sol.minMutation(start, end, bank), expected)

    def test_case_3(self):
        sol = Solution()
        start = "AAAAACCC"
        end = "AACCCCCC"
        bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
        expected = 3
        self.assertEqual(sol.minMutation(start, end, bank), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
