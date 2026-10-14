class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def mergeTwoIntervals(a: List[int], b: List[int]) -> List[int]:
            return [
                min(a[0], b[0]),
                max(a[1], b[1])
            ]
        
        res = []

        # Phase 1: skip all the intervals we don't need to touch
        i = 0
        while i < len(intervals) and intervals[i][0] <= newInterval[0] :
            res.append(intervals[i])
            i += 1
        
        # Check if we need to merge or insert:
        if res==[] or res[-1][1] < newInterval[0]:
            res.append(newInterval)
        else:
            res[-1] = mergeTwoIntervals(res[-1], newInterval)
        
        # Merge or append the remaining intervals
        while i < len(intervals):
            if intervals[i][0] <= res[-1][1]:
                res[-1] = mergeTwoIntervals(intervals[i], res[-1])
            else:
                res.append(intervals[i])
            i += 1
                
        return res
        

     


        