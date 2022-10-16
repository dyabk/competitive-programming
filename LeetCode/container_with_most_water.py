class Solution:
    def maxArea(self, height: List[int]) -> int:
        absMax = 0
        l, r = 0, len(height) - 1
        while l < r:
            curArea = (r - l) * min(height[l], height[r])
            absMax = max(curArea, absMax)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return absMax
