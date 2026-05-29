class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        m = 0
        while l < r:
            width = r - l
            length = min(heights[l], heights[r])
            if width * length > m:
                m = width * length
            
            if heights[l+1] > heights[r-1]:
                l += 1
            else:
                r -= 1
        return m