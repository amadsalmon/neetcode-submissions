import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(heap)
        
        for _ in range(k):
            (smallest, index) = heapq.heappop(heap)
            nums[index] = smallest * multiplier
            heapq.heappush(heap, (nums[index], index))
        
        return nums


        