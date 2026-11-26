from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def isPathAbsolutelyPossible() -> bool:
            srcSeen = False
            dstSeen = False
            for s, d, _ in flights:
                    if s == src:
                        srcSeen = True
                    if d == dst: 
                        dstSeen = True
            
            if not srcSeen or not dstSeen:
                return False
            return True
        
        def buildAdjacencyList() -> dict:        
            memo = {}
            for i in range(n):
                memo[i] = []
            
            for source, destination, price in flights:
                memo[source].append((destination, price))

            return memo

        if not isPathAbsolutelyPossible(): 
            return -1

        adjList = buildAdjacencyList()
        heap = []

        # We start at city dst and put all the destinations reachable by dst in the heap
        for destination, price in adjList[src]:
            heappush(heap, (price, 1, destination))
        
        # Dkjistra's algorithm adapted
        while heap:
            current_cost, current_stops, current_destination = heappop(heap)
            if current_destination == dst:
                return current_cost
            if current_stops >= k + 1:
                continue ## i dont want to return i just want to drop this path. 
            for destination, price in adjList[current_destination]:
                heappush(heap, (current_cost + price, current_stops + 1, destination))

        return -1






