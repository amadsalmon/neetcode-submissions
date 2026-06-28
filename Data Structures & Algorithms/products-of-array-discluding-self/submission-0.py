class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        i = 0

        while i < len(nums):
            x = 0
            while x < len(nums):
                if x != i:
                    output[i] *= nums[x]
                x += 1 
            i += 1

        return output