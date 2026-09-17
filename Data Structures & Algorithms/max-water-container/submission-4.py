class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        start = 0
        end = len(heights) - 1
        maxArea = 0

        while end > start:
            maxArea = max(maxArea, (min(heights[start], heights[end]) * end - start))

            if heights[start] > heights[end]:
                end -= 1
            elif heights[start] <= heights[end]:
                start += 1

        return maxArea

