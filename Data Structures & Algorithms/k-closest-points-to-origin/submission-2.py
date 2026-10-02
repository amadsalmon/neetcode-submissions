from heapq import heapify, heappush, heappushpop, heappop

class Solution:
    """
    Implementation with a min-heap

    Total time complexity: O(N) for initial pass + O(N) for heapifying + O(k*log(n)) for popping the k closest elements.
    Space complexity:      O(N), because we created a heap size of N. that's all        
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def computeEuclideanDistanceToRoot(x: int, y: int) -> float:
            import math
            # noting that we don't even need to compute sqrt here, comparison will not matter with or without it
            return math.sqrt(math.pow(x, 2) + math.pow(y, 2))  

        max_heap = []
        heapify(max_heap)

        for [x,y] in points:
            distance = computeEuclideanDistanceToRoot(x, y)
            if len(max_heap) >= k and max_heap[0][0] < distance:
                heappushpop(max_heap, (-1 * distance, [x,y]))
            else:
                heappush(max_heap, (-1 * distance, [x,y]))


        return [heappop(max_heap)[1] for _ in range(k)]
