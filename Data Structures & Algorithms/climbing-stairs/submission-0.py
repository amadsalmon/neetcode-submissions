from collections import defaultdict

class Solution:

    def climbStairs(self, n: int) -> int:
        
        memo = defaultdict(int)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2

        def _climb(n: int, memo: defaultdict) -> int:
            if n in memo:
                return memo[n]
            else:
                memo[n] = _climb(n-1, memo) + _climb(n-2, memo)
                return memo[n]
        
        return _climb(n, memo)