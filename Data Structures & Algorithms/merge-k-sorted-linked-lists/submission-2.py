# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heapify, heappush, heappop

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        # Merge all K linked lists into a single mega linked list: O(N)
        mega_heap = []
        for l in lists:
            node = l
            while node:
                mega_heap.append(node.val)
                node = node.next
        heapify(mega_heap)
        
        # Start merging
        dummy = ListNode(-99999)
        current = dummy
        while mega_heap:
            min_found = heappop(mega_heap)
            current.next = ListNode(min_found)
            current = current.next

        return dummy.next

        

        