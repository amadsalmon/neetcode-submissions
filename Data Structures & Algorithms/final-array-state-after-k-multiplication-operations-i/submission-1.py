class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for i in range(k):

            min_i = -1
            min_n = max(nums)
            for i in range(len(nums)):
                if nums[i] < min_n:
                    min_n = nums[i]
                    min_i = i
            
            nums[min_i] = min_n * multiplier
        
        return nums

        