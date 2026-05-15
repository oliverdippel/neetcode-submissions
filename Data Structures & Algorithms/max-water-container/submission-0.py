class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water_volume = 0

        left, right = 0, len(heights)-1

        while left < right:
            min_height = min(heights[left], heights[right])
            current_water_volume = min_height * (right - left)
            max_water_volume = max(max_water_volume, current_water_volume)

            if heights[left] > heights[right]:
                right -=1
            else:
                left += 1
        
        return max_water_volume