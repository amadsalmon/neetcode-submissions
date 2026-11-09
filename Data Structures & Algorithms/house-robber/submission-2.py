class Solution:
    def rob(self, houses: List[int]) -> int:
        N = len(houses) - 1
        memo = {}

        def robber(i: int) -> int:
            if i == 0:
                return houses[0]
            elif i < 0: 
                return 0

            if i not in memo:
                memo[i] = max(
                    houses[i] + robber(i - 2),
                    robber(i - 1)
                )
            return memo[i]

        return robber(N)