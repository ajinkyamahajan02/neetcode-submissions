class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0

        head = 0
        tail = len(heights)-1

        while head < tail:

            tempArea = (tail - head) * (min(heights[tail], heights[head]))

            if tempArea > maxArea:
                maxArea = tempArea

            if heights[head] > heights[tail]:
                tail -= 1
            else:
                head += 1
            
        return maxArea