from functools import lru_cache

class Solution:
    """
    Now implemented with a LRU cache
    """
    def tribonacci(self, n: int) -> int:
        if n < 0: return 0
        
        @lru_cache
        def _tribonacci(n: int) -> int:
            if n == 0: return 0
            if n == 1 or n == 2: return 1
            return _tribonacci(n-1) + _tribonacci(n-2) + _tribonacci(n-3)
        
        return _tribonacci(n)

    """
    Top-down memoization solution.
    """
    def tribonacci_v0(self, n: int) -> int:
        if n < 0: return 0

        memo = defaultdict(int)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        def _tribonacci(n: int) -> int:
            if n in memo: return memo[n]
            result = _tribonacci(n-1) + _tribonacci(n-2) + _tribonacci(n-3)
            memo[n] = result
            return result
        
        return _tribonacci(n)
        