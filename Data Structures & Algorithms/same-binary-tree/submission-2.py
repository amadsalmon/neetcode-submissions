from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Three solutions implemented below:
1. Recursive:
2. Iterative, using a stack.
3. Iterative, using a queue.
"""

class Solution:
    def isSameTree_recursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (not p and q): return False
        if not p and not q: return True
        if p.val != q.val: return False
        return self.isSameTree_recursive(p.left, q.left) and self.isSameTree_recursive(p.right, q.right)
            

    def isSameTree_stack(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []

        stack.append(p)
        stack.append(q)

        while stack:
            p = stack.pop()
            q = stack.pop()

            if (p and not q) or (not p and q): return False
            if (not p and not q):
                continue
            if p.val != q.val: return False

            stack.append(p.left)
            stack.append(q.left)
            stack.append(p.right)
            stack.append(q.right)

        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()

        queue.append(p)
        queue.append(q)

        while queue:
            p = queue.popleft()
            q = queue.popleft()

            if (p and not q) or (not p and q): return False
            
            if (not p and not q):
                continue

            if p.val != q.val: return False

            queue.append(p.left)
            queue.append(q.left)
            queue.append(p.right)
            queue.append(q.right)

        return True


            