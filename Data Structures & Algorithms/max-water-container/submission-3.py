class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = max(maxArea, (min(heights[start], heights[end]) * end - start))

        if heights[start] > heights[end]:
            end -= 1
        elif heights[start] <= heights[end]:
            start += 1

        return maxArea