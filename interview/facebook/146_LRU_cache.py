import unittest
from typing import List
from pprint import pprint

import collections


class LRUCache1:
    # use built-in data structure

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict.move_to_end(key, True)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.move_to_end(key, True)
        self.dict[key] = value
        if len(self.dict) > self.cap:
            self.dict.popitem(last=False)

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)


class Node:
    def __init__(self, k=None, v=None, prv=None, nxt=None) -> None:
        self.k = k
        self.v = v
        self.prv = prv
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {}
        self.sentinel = Node()
        self.end = Node(prv=self.sentinel)
        self.sentinel.nxt = self.end

    def _evit(self, node):
        prv, nxt = node.prv, node.nxt
        prv.nxt, nxt.prv = nxt, prv

    def _append(self, node):
        cur_end = self.end.prv
        cur_end.nxt = node
        node.prv = cur_end
        node.nxt = self.end
        self.end.prv = node

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self._evit(node)
        self._append(node)
        return node.v

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            node = Node(key, value)
            self.dict[key] = node
            self._append(node)
            if len(self.dict) > self.cap:
                to_evict = self.sentinel.nxt
                self._evit(to_evict)
                self.dict.pop(to_evict.k)
        else:
            self.get(key)
            self.dict[key].v = value


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
