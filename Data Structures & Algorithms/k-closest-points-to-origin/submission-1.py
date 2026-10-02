from heapq import heapify, heappop

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

        distances_per_point = [(computeEuclideanDistanceToRoot(x, y), [x, y]) for [x,y] in points]

        heapify(distances_per_point)

        return [heappop(distances_per_point)[1] for _ in range(k)]
