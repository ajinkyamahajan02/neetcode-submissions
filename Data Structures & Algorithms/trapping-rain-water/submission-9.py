class Solution:
    def trap(self, height: List[int]) -> int:
        l = height[0]
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        maxWater = 0

        while l < r:
            if maxL < maxR:
                maxWater += max(0, maxL - height[l])
                l += 1
                maxL = max(maxL, height[l])
            else:
                maxWater += max(0, maxR - height[r])
                r -= 1
                maxR = max(maxR, height[r])

        return maxWater
            