class Solution:
    """
    Example:

    Base intervals = [[1,3] [6,8] [9, 15]]

    Multiple cases based on input newInterval:
    1. non overlapping at all : [4,5]
    2. overlapping one interval: [2,4], need to merge [1,3] 
    3. overlapping multiple intervals: [2, 12] , need to merge [1,3] [6,8] [9,15] together (really an over-case of overlapping one interval)
    4. Also there's the case where the overlap is not complete e.g. needing to merge 2,4 and 1,3 results in 1,4 where we took the outer boundaries of each.
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def mergeTwoIntervals(a: List[int], b: List[int]) -> List[int]:
            return [
                min(a[0], b[0]),
                max(a[1], b[1])
            ]

        def shouldInsertAfter(a: List[int], b: List[int]) -> bool:
            return a[1] < b[0]

        def areMergeable(a: List[int], b: List[int]) -> bool:
            return a[1] >= b[0]

        if intervals == []:
            intervals.append(newInterval)

        # Find first interval where newInterval can belong
        i = 0
        while i < len(intervals) and intervals[i][0] <= newInterval[0]:
            i += 1
        if i > 0:
            i -= 1

        # Check if there's overlap at all:
        if i == 0 and intervals[0][0] > newInterval[1]:
            intervals.insert(0, newInterval) 
        elif shouldInsertAfter(intervals[i], newInterval):
            intervals.insert(i+1, newInterval) 
            i += 1
        else:
            # Replace old interval with merged one
            intervals[i] = mergeTwoIntervals(intervals[i], newInterval)
        
        # Now check if there's overlap with the next intervals:
        while i < len(intervals) - 1 and areMergeable(intervals[i], intervals[i+1]):
            intervals[i] = mergeTwoIntervals(intervals[i], intervals[i+1])
            intervals.pop(i+1)   
                
        return intervals
 

        
        
