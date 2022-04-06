import unittest
from typing import List
from pprint import pprint

import collections


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        counter = collections.Counter(arr)
        seen = []
        seen_set = set()
        vals = sorted(counter.keys())
        res = 0

        def two_sum(target):
            res = 0
            i = 0
            j = len(seen)-1
            while i < j:
                ni = seen[i]
                nj = seen[j]
                s = ni + nj
                if s == target:
                    res += counter[ni]*counter[nj]
                    i += 1
                    j -= 1
                elif s < target:
                    i += 1
                else:
                    j -= 1
            if i == j and seen[i]*2 == target and counter[seen[i]] >= 2:
                res += int(counter[seen[i]]*(counter[seen[i]]-1) / 2)
            return res

        for n in vals:
            res += counter[n]*two_sum(target-n) % MOD
            # print('a', res)
            cnt = counter[n]
            if n*3 == target:
                if cnt >= 3:
                    res += int(cnt * (cnt-1) * (cnt-2) / 6)
                    # print('b', res)
            elif (target-n*2) in seen_set and cnt >= 2:
                res += int(cnt * (cnt-1) * counter[target-n*2] / 2)
                # print('c', res)
            # print('d', n, res)
            seen.append(n)
            seen_set.add(n)

        return res % MOD


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        target = 8
        expected = 20
        self.assertEqual(sol.threeSumMulti(arr, target), expected)

    def test_case_2(self):
        sol = Solution()
        arr = [1, 1, 2, 2, 2, 2]
        target = 5
        expected = 12
        self.assertEqual(sol.threeSumMulti(arr, target), expected)

    def test_case_3(self):
        sol = Solution()
        arr = [0, 2, 0]
        target = 2
        expected = 1
        self.assertEqual(sol.threeSumMulti(arr, target), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
