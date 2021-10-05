import unittest
from typing import List
from pprint import pprint

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator1:
    """
    use an array to save all the elements
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nums = []
        while iterator.hasNext():
            self.nums.append(iterator.next())
        self.i = 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nums[self.i]

    def next(self):
        """
        :rtype: int
        """
        n = self.peek()
        self.i += 1
        return n

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.nums)


class PeekingIterator2:
    """
    by caching one element
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iter = iterator
        self.cur_ele, self.nxt_ele = None, self._iter.next() if self._iter.hasNext() else None
        self.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cur_ele

    def next(self):
        """
        :rtype: int
        """
        tmp_cur_ele = self.cur_ele
        self.cur_ele = self.nxt_ele
        self.nxt_ele = self._iter.next() if self._iter.hasNext() else None
        return tmp_cur_ele

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur_ele != None


class PeekingIterator3:
    """
    Google Guawa Implementation:
    https://github.com/google/guava/blob/703ef758b8621cfbab16814f01ddcc5324bdea33/guava-gwt/src-super/com/google/common/collect/super/com/google/common/collect/Iterators.java#L1125
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.has_peeked = False
        self.peeked_ele = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.has_peeked:
            return self.peeked_ele
        self.has_peeked = True
        self.peeked_ele = self.iterator.next()
        return self.peeked_ele

    def next(self):
        """
        :rtype: int
        """
        if self.has_peeked:
            self.has_peeked = False
            ele = self.peeked_ele
            self.peeked_ele = None
            return ele
        else:
            return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_peeked or self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


class PeekingIterator:
    """
    by caching one element
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._has_next = False
        self._next = None
        self.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next

    def next(self):
        """
        :rtype: int
        """
        ret = self._next
        self._has_next = self.iterator.hasNext()
        self._next = self.iterator.next() if self._has_next else None
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._has_next


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
