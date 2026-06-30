class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        left = 0
        right = len(heights)-1

        while left < right:
            if heights[left] <= heights[right]:
                vol = (right - left) * heights[left]
                left += 1
            else:
                vol = (right - left) * heights[right]
                right -= 1

            if vol > max_vol: 
                max_vol = vol

        return max_vol