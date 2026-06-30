class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        left = 0
        right = len(heights)-1

        while left < right:
            vol = (right - left) * min(heights[left], heights[right])

            if vol > max_vol: 
                max_vol = vol

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_vol


        