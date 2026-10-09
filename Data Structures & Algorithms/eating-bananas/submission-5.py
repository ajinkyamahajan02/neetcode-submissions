from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = float("infinity")
        head = 1
        tail = max(piles)

        while head <= tail:
            mid  = int((head + tail) / 2)
            tempHours = 0
            for element in piles:
                tempHours += ceil(element / mid)

            if tempHours < h:
                minSpeed = min(minSpeed, mid)
                tail = mid - 1

            if tempHours > h:
                head = mid + 1
        return minSpeed