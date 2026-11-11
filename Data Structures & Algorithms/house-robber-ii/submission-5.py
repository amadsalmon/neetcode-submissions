class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        LAST_IDX = N - 1

        def robber(range_start: int, range_end: int) -> int:
            if len(nums) == 1: return nums[0]
            if range_start < 0 or range_end > LAST_IDX:
                return 0

            a, b = 0, nums[range_start]
            i = range_start + 1
            while i <= range_end:
                tmp = b
                b = max(b, a + nums[i])
                a = tmp
                i += 1
            
            return b
        
        return max(
            robber(0, LAST_IDX - 1),
            robber(1, LAST_IDX)
        )
        