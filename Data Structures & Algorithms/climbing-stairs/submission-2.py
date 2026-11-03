from collections import defaultdict


"""
What are the different ways we can get to step n?
Two ways we can get there: from step n-1, or from step n-2. 

Par récurrence
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}

        d[0] = 1
        d[1] = 1
        d[2] = 2

        def helper(n: int, memo: dict) -> int:
            if n < 0: 
                return 0
            if n in memo: 
                return memo[n]
        
            memo[n] = helper(n-1, memo) + helper(n-2, memo)
            return memo[n]

        return helper(n, d)
