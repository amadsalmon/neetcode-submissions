# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        
        for i in range(0, int((len(arr))/2)):
            if i != len(arr)-i-1 and arr[i] != arr[len(arr)-i-1]:
                return False
        return True
        