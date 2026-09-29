# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b: return True
            if (not a and b) or (a and not b): return False
            if a.val != b.val: return False
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)
        
        if not root: return False
        
        queue  = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if sameTree(node, subRoot): 
                return True
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return False
                