from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * stone for stone in stones]  # to make the default min-heap a max-heap
        heapify(heap)

        while len(heap) > 1:
            stone_x = heappop(heap) * -1
            stone_y = heappop(heap) * -1
            if stone_x == stone_y:
                continue
            elif stone_x < stone_y:
                heappush(heap, (stone_y - stone_x) * -1)
            else: 
                heappush(heap, (stone_x - stone_y) * -1)
    
        return heappop(heap) * -1 if len(heap) == 1 else 0
