from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #return self.minCostClimbingStairs_topdown(cost)
        return self.minCostClimbingStairs_bottomup(cost)

    def minCostClimbingStairs_topdown(self, cost: List[int]) -> int:
        """
        Time and space complexities are both O(N)
        Space comes from the fact we're storing N+1 entries and recursion is N deep too.
        We can do better on space by going bottom up and discarding the memo because actually 
        all we need is values of n-1 and n-2!
        """
        N = len(cost)
        memo = {}  # functools.@cache would do this in one line
 
        def helper(i: int) -> int:
            if i <= 1:
                return 0 # Starting from position 0 or 1 is free
            if i not in memo:
                memo[i] = min(
                    helper(i-1) + cost[i-1],
                    helper(i-2) + cost[i-2]
                )
            return memo[i]

        return helper(N)

    def minCostClimbingStairs_bottomup(self, cost: List[int]) -> int:
        """Time complexity: O(N). Space complexity: O(1)"""
        a, b = cost[0], cost[1]

        for i in range(2, len(cost)):
            new = cost[i] + min(a, b)
            a = b
            b = new

        return min(a, b)
