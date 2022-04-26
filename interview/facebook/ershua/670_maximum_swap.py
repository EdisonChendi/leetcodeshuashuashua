import enum
import unittest
from typing import List
from pprint import pprint


class Solution1:
    def maximumSwap(self, num: int) -> int:
        counter = [[] for _ in range(10)]
        ns = []
        n = num
        i = 0
        while n > 0:
            n, r = divmod(n, 10)
            counter[r].append(i)
            ns.append(r)
            i += 1

        j = 9
        for i in reversed(range(len(ns))):
            n = ns[i]
            while j >= 0 and len(counter[j]) == 0:
                j -= 1
            if n == j:
                counter[n].pop()
            else:
                swap = counter[j][0]
                ns[i], ns[swap] = ns[swap], ns[i]
                break
        return sum(ns[i]*10**i for i in range(len(ns)))


class Solution:
    def maximumSwap(self, num: int) -> int:
        ns = []
        max_v = -1
        m = l = r = -1
        i = 0
        while num > 0:
            num, rem = divmod(num, 10)
            ns.append(rem)

            if rem > max_v:
                max_v = rem
                m = i
            elif rem < max_v:
                l, r = i, m
            i += 1

        ns[l], ns[r] = ns[r], ns[l]
        return sum(n*10**i for i, n in enumerate(ns))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = 2736
        expected = 7236
        self.assertEqual(sol.maximumSwap(num), expected)

    def test_case_2(self):
        sol = Solution()
        num = 9973
        expected = 9973
        self.assertEqual(sol.maximumSwap(num), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
