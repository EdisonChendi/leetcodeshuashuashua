from tokenize import cookie_re
import unittest
from typing import List
from pprint import pprint
import collections
import heapq


class Solution1:
    def maximumSwap(self, num: int) -> int:
        arr = []
        h = []
        aux_dict = collections.defaultdict(set)
        i = 0
        while num > 0:
            num, d = divmod(num, 10)
            arr.append(d)
            heapq.heappush(h, -d)
            aux_dict[d].add(i)
            i += 1

        for j in reversed(range(i)):
            d = arr[j]
            if d == -h[0]:
                aux_dict[d].remove(j)
                heapq.heappop(h)
            else:
                idx = min(aux_dict[-h[0]])
                arr[j], arr[idx] = arr[idx], arr[j]
                break

        res = 0
        for n in reversed(arr):
            res = res * 10 + n
        return res


class Solution2:
    def maximumSwap(self, num: int) -> int:
        arr = []
        temp = num
        while temp > 0:
            temp, rem = divmod(temp, 10)
            arr.append(rem)

        N = len(arr)
        last = {}
        for i in reversed(range(N)):
            n = arr[i]
            last[n] = i

        res = 0
        for i in reversed(range(N)):
            n = arr[i]
            for d in reversed(range(10)):
                if n >= d:
                    break

                if d in last and last[d] < i:
                    arr[i], arr[last[d]] = arr[last[d]], arr[i]

                    for n in reversed(range(i+1)):
                        res = res * 10 + arr[n]
                    return res
            res = res * 10 + n
        return num


class Solution:
    def maximumSwap(self, num: int) -> int:
        max_val = -1
        m = l = r = -1
        arr = []
        i = 0
        while num > 0:
            num, rem = divmod(num, 10)
            arr.append(rem)

            if rem > max_val:
                max_val, m = rem, i
                m = i
            elif rem < max_val:
                l, r = i, m
            i += 1

        arr[l], arr[r] = arr[r], arr[l]
        return sum(n*10**i for i, n in enumerate(arr))


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

    def test_case_3(self):
        sol = Solution()
        num = 9979
        expected = 9997
        self.assertEqual(sol.maximumSwap(num), expected)

    def test_case_4(self):
        sol = Solution()
        num = 129979
        expected = 929971
        self.assertEqual(sol.maximumSwap(num), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
