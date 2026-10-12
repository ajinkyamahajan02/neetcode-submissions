from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        head = 1
        tail = max(piles)
        maxSpeed = float("infinity")

        while head <= tail: 
            mid = int((head + tail) / 2)

            tempHours = 0
            for element in piles:
                tempHours += ceil(element / mid)

            if tempHours <= h:
                maxSpeed = min(maxSpeed, mid)
                tail = mid - 1

            if tempHours > h:
                head = mid + 1

        return maxSpeed