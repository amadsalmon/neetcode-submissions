class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n - 1
            while j < k:
                if nums[i] == -nums[j] - nums[k]:
                    res.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j += 1
                    k -= 1
                elif nums[i] > -nums[j] - nums[k]:
                    k -= 1
                elif nums[i] < -nums[j] - nums[k]:
                    j += 1

        return res

            



            

        