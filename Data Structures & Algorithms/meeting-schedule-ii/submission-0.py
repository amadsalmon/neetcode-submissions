from heapq import heapify, heappop, heappush, heappushpop

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = [(i.start, i.end) for i in intervals]
        intervals.sort()  # O(N * log N)
        
        if not intervals:
            return 0

        heap = [] 
        heapify(heap)
        heappush(heap, -1)

        for (i_start, i_end) in intervals:
            if heap[0] > i_start:
                heappush(heap, i_end)
            else:
                heappushpop(heap, i_end)
        
        return len(heap)
