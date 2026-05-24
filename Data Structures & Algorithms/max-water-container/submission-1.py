class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_volume = -1
        while left < right:
            width = right - left
            current_height = min(heights[left], heights[right])
            current_volume = width * current_height
            max_volume = max(current_volume, max_volume)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return max_volume