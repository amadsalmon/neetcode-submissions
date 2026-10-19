# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:            
        if not root: return []
        
        cache = {}

        q = deque()
        q.append((root, 0))

        while q:
            node, height = q.popleft()
            cache[height] = node.val
                
            if node.left: q.append((node.left, height + 1))
            if node.right: q.append((node.right, height + 1))

        return [val for val in cache.values()]

