from heapq import heapify, heappush, heappop
class KthLargest:
    """
    Min heap stores elements in increasing order.
    So if we use it to store only k elements, and we kick out (pop) the 
    smallest element each time a new one enters the stream, we're sure to keep the top K largest elements.
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)

        # Ensure heap stores k elements at most, the k largest of the initial array
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
        
