class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        res = 0
        maxL = -float("infinity")
        maxR = -float("infinity")

        while left < right:
            maxL = max(maxL, height[left])
            maxR = max(maxR, height[right])

            if maxL < maxR:
                res += max(min(maxL, maxR) - height[left], 0)
                left += 1
            else:
                res += max(min(maxL, maxR) - height[right], 0)
                right -= 1

        return res

