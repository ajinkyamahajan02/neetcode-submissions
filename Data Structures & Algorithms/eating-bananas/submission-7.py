from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        maxPile = max(piles)
        head = 1
        tail = maxPile
        minBananas = float("infinity")

        while head <= tail:
            mid = int((head + tail) / 2)
            tempHours = 0
            for element in piles:
                tempHours += ceil(element / mid)

            if tempHours <= h:
                minBananas = min(minBananas, mid)
                tail = mid - 1

            elif tempHours > h:
                head = mid + 1

        return minBananas
        