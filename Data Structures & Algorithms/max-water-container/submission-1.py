class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_max = 0
        l, r = 0, len(heights) - 1

        while l < r:
            volume = min(heights[l], heights[r]) * (r - l)
            if volume > current_max:
                current_max = volume
            else:
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
        
        return current_max
