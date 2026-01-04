class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        l = 0
        r = n - 1
        
        while r != l:
            area = max(area, (r-l)*min(height[r], height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area
