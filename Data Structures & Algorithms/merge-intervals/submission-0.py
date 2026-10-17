class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def isOverlap(a: List[int], b: List[int]) -> bool:
            # Assumes a[0] <= b[0]
            return a[1] >= b[0]

        def merge(a: List[int], b: List[int]) -> bool:
            return [
                min(a[0], b[0]),
                max(a[1], b[1])
            ]
        
        if not intervals:
            return []

        intervals.sort()
        res = [intervals[0]] 

        i = 1
        while i < len(intervals):
            if isOverlap(res[-1], intervals[i]):
                res[-1] = merge(res[-1], intervals[i])
            else:
                res.append(intervals[i])

            i += 1
        
        return res