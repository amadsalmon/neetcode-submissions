class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.canJump_dpbu(nums)

    def canJump_dpbu(self, nums: List[int]) -> bool:
        """Dynamic programming - Bottom Up"""
        dp = [False] * len(nums)  # dp[i] means i is reacheable from 0
        dp[0] = True

        for i, max_jump in enumerate(nums):
            if dp[i] != 0:
                for j in range(i + 1, min(i + max_jump + 1, len(dp))):
                    dp[j] = True

        return dp[-1]