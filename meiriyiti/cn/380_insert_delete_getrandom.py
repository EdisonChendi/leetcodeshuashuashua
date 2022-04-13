import unittest
from typing import List
from pprint import pprint

import random
class RandomizedSet1:

    def __init__(self):
        self.set = set()
        self.arr = []
        self.i = 0

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.arr.append(val)
        self.set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        self.arr.remove(val)
        return True

    def getRandom(self) -> int:
        while True:
            idx = random.randint(self.i, len(self.arr)-1)
            n = self.arr[idx]
            if n in self.set:
                return n
            self.arr[idx], self.arr[idx] = self.arr[idx], self.arr[idx]
            self.i += 1

class RandomizedSet:

    def __init__(self):
        self.val_pos = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.val_pos:
            return False
        self.val_pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_pos:
            return False
        pos = self.val_pos[val]
        self.arr[pos] = self.arr[-1]
        self.val_pos[self.arr[-1]] = pos
        self.val_pos.pop(val)
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0,len(self.arr)-1)]

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass
        
    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
