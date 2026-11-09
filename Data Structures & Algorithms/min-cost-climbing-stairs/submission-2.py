from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)

        @cache
        def helper(i: int) -> int:
            if i <= 1:
                # Starting from position 0 or 1 is free
                return 0
            
            return min(
                helper(i-1) + cost[i-1],
                helper(i-2) + cost[i-2]
            )

        return helper(N)
        
