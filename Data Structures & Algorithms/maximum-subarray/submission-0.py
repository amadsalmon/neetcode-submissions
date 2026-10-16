class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        l, r, n = 0, 0, len(nums)
        
        running_sum = 0
        max_sum = float('-inf')

        while r < n:
            running_sum += nums[r]
            max_sum = max(max_sum, running_sum) 
            r += 1
            if running_sum < 0:
                # Drop current subsequence
                l = r
                running_sum = 0

        return max_sum
