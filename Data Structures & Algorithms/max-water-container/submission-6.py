class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        start = 0
        end = len(heights) - 1
        maxArea = 0

        while start < end:
            area = min(heights[start], heights[end]) * (end - start)
            maxArea = max(maxArea, area)

            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1

        return maxArea

