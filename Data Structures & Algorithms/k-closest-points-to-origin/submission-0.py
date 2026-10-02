from heapq import heapify, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def computeEuclideanDistanceToRoot(x: int, y: int) -> float:
            import math
            return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

        distances_per_point = [(computeEuclideanDistanceToRoot(x, y), [x, y]) for [x,y] in points]

        heapify(distances_per_point)

        return [heappop(distances_per_point)[1] for _ in range(k)]

        