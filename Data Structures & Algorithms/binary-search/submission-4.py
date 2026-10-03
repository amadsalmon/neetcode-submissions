class Solution:
    """
    Classic binary search problem, doable in O(log N).
    Could use the Python bisect solution but I'll implement binary search manually
    """
    def search_manual(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        import bisect
        idx = bisect.bisect_left(nums, target)
        return idx if idx < len(nums) and nums[idx] == target else -1