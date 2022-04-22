import unittest
from typing import List
from pprint import pprint


class MyHashMap:

    def __init__(self):
        self.size = 100
        self.arr = [None]*self.size

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        if self.arr[idx] is None:
            self.arr[idx] = [(key, value)]
        else:
            for i, (k, _) in enumerate(self.arr[idx]):
                if k == key:
                    self.arr[idx][i] = (key, value)
                    return
            self.arr[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = key % self.size
        if self.arr[idx] is None:
            return -1
        lst = self.arr[idx]
        for k, v in lst:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        if self.get(key) == -1:
            return

        lst = self.arr[key % self.size]
        for i in range(len(lst)):
            if lst[i][0] == key:
                break
        else:
            return
        self.arr[key % self.size] = lst[:i]+lst[i+1:]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
