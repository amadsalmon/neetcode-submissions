class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #return self.canJump_dpbu(nums)
        return self.canJump_greedy(nums)

    def canJump_dpbu(self, nums: List[int]) -> bool:
        """
        Dynamic programming - Bottom Up
        Time: O(N^2)  Space: O(N)
        """
        dp = [False] * len(nums)  # dp[i] means i is reacheable from 0
        dp[0] = True

        for i, max_jump in enumerate(nums):
            if dp[i] != 0:
                for j in range(i + 1, min(i + max_jump + 1, len(dp))):
                    dp[j] = True

        return dp[-1]
    

    def canJump_greedy(self, nums: List[int]) -> bool:
        """
        Greedy approach.
        Time: O(N)  Space: O(1)
        """
        max_reach = 0
        for i, max_jump in enumerate(nums):
            if i > max_reach: 
                return False
            
            max_reach = max(max_reach, i + max_jump)
            
            if max_reach >= len(nums) - 1:
                return True
            

        return max_reach >= len(nums) - 1