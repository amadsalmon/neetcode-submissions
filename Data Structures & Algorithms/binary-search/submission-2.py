class Solution:
    def search_rec(self, nums: List[int], target: int, start: int, end: int) -> int:
        if start > end or target < nums[start] or target > nums[end]:
            return -1
        
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.search_rec(nums, target, mid + 1, end)
        else:
            return self.search_rec(nums, target, start, mid - 1)
        
        return -1


    def search(self, nums: List[int], target: int) -> int:
        return self.search_rec(nums, target, 0, len(nums) - 1)
        