class Solution:
    def trap(self, height: List[int]) -> int:
        l = heights[0]
        r = len(heights) - 1
        maxL = heights[l]
        maxR = heights[r]
        maxWater = 0

        while l < r:
            if maxL < maxR:
                maxWater += max(0, maxL - heights[l])
                l += 1
                maxL = max(maxL, heights[l])
            else:
                maxWater += max(0, maxR - heights[r])
                r -= 1
                maxR = max(maxR, heights[r])

        return maxWater
            