# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, None)
        l_sum = dummy

        carryover = 0
        while l1 or l2 or carryover:
            current_sum = 0

            if l1:
                current_sum += l1.val
                l1 = l1.next
            if l2:
                current_sum += l2.val
                l2 = l2.next

            current_sum += carryover
            
            if current_sum >= 10:
                current_sum -= 10
                carryover = 1
            else:
                carryover = 0
            
            l_sum.next = ListNode(current_sum)
            l_sum = l_sum.next
        
        return dummy.next
        

        