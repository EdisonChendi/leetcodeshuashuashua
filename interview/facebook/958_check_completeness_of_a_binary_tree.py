import collections
import unittest
from typing import List
from pprint import pprint

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # BFS
        cur = [root]
        flag = False
        while cur:
            nxt = []
            for node in cur:
                left, right = node.left, node.right
                if flag:
                    if left or right:
                        return False
                else:
                    if not left and right:
                        return False
                    elif left and not right:
                        flag = True
                        nxt.append(left)
                    elif not left and not right:
                        flag = True
                    else:
                        nxt.append(left)
                        nxt.append(right)
            cur = nxt
        return True


class Solution2:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # BFS
        q = collections.deque([root])
        end = False
        while q:
            node = q.popleft()
            if end and node:
                return False
            if node:
                q.extend([node.left, node.right])
            else:
                end = True
        return True


class Solution3:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # BFS
        i = 0
        q = [root]
        while q[i]:
            q.append(q[i].left)
            q.append(q[i].right)
            i += 1
        # return not any(q[j] for j in range(i+1, len(q)))
        return not any(q[i+1:])


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # DFS
        def count(node):
            if not node:
                return 0
            return 1+count(node.left)+count(node.right)

        def helper(node, idx):
            if not node:
                return True

            if idx >= total:
                return False

            return helper(node.left, 2*idx+1) and helper(node.right, 2*idx+2)

        total = count(root)
        return helper(root, 0)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
