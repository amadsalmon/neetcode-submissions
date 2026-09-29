# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()

        queue.append(p)
        queue.append(q)

        while queue:
            p = queue.pop()
            q = queue.pop()

            if (p and not q) or (not p and q): return False
            
            if (not p and not q):
                continue

            if p.val != q.val: return False

            queue.append(p.left)
            queue.append(q.left)
            queue.append(p.right)
            queue.append(q.right)

        return True
            