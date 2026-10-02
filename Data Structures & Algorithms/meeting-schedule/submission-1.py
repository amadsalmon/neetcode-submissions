"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = [(i.start, i.end) for i in intervals]
        intervals.sort()  # O(N * log N) - dominates
        
        last_end = -1
        for i_start, i_end in intervals: # O(N)
            if i_start < last_end:
                return False
            last_end = i_end
        return True