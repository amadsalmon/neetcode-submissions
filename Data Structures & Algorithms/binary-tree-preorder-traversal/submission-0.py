# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], order: List[int]) ->  List[int]:
        if not root:
            return order
        
        order.append(root.val)

        #print(f"\nExploring and appended {root.val} to order (now order={order})")

        if root.left:
            #print(f" - Exploring left {root.left.val} of {root.val} ; (now order={order})")
            
            self.traverse(root.left, order)
        
        if root.right:
            #print(f" - Exploring right {root.right.val} of {root.val} ; (now order={order})")
            
            self.traverse(root.right, order)

        #print(f"-> Finished Exploring {root.val}. Returning {order}")
        return order
        

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root, [])
        