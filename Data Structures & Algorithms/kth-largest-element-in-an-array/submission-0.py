from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(heap)

        for i in range(len(heap)-k):
            heapq.heappop(heap)
        
        return heap[0]



        