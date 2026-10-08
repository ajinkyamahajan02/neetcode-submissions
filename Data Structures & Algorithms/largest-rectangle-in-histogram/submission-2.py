class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxArea = 0

        for i,h in enumerate(heights):
            while stk and stk[-1][1] > h:
                index, height = stk.pop()
                maxArea = max(maxArea, height * (i - index))
                start = i
            stk.append([start, h])

        for i,h in stk:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
