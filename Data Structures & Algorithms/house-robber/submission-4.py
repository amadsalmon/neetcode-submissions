class Solution:
    def rob(self, houses: List[int]) -> int:
        #return self.rob_topdown(houses)
        return self.rob_bottomup_tab(houses)
    
    def rob_topdown(self, houses: List[int]) -> int:
        """
        Top-down dynamic programming with memoization
        Time: O(N). Space: O(N).
        """
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
    
    def rob_bottomup_tab(self, houses: List[int]) -> int:
        """
        Bottom-up dynamic programming with tabulation
        Time: O(N). Space: O(N).
        """
        N = len(houses) 
        dp = [0] * N
        dp[0] = houses[0]

        for i in range(1, N):
            dp[i] = max(
                houses[i] + dp[i-2],
                dp[i-1]
            )

        return dp[N-1]


