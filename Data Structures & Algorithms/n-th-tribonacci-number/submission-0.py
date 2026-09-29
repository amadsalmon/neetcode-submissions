class Solution:
    def tribonacci(self, n: int) -> int:
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
        