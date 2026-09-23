class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)
        maxL = height[left]
        maxR = height[right]
        water = 0

        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                water += max(0, min(maxR, maxL)-height[left])
            else:
                right -= 1
                maxR = max(maxR, height[right])
                water += max(0, min(maxR, maxL)-height[right])
        return water
