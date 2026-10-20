# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, maxVal: int):
            if not node:
                return 0

            if node.val >= maxVal:
               return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)

            return dfs(node.left, maxVal) + dfs(node.right, maxVal)


        return dfs(root, root.val)
            