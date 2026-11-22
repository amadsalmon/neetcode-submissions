class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target =  n * (n + 1) // 2

        for i in range(0,len(nums)):
            target -= nums[i]

        return target
        