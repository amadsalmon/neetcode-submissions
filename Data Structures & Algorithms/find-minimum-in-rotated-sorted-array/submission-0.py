class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums) 
        l = 0 
        r = n - 1

        while l < r:
            mid = (l + r) // 2
                      
            # If mid element is greater than the rightmost element,
            # the minimum must be in the right half (excluding mid).
            # e.g. 4..9..2
            if nums[mid] > nums[r]:
                l = mid + 1
            
            # Otherwise, the minimum is at mid or in the left half.
            # e.g. 2..4..9
            else:
                r = mid
        return nums[l]