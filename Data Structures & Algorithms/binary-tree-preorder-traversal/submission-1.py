# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node: Optional[TreeNode], order: List[int]) ->  List[int]:
        if not node:
            return order
        
        order.append(node.val)
        self.traverse(node.left, order)
        self.traverse(node.right, order)

        return order
        

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root, [])
        