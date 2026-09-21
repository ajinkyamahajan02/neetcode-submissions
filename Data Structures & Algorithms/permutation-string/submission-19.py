class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        winLen = len(s1)
        r = 0

        while r < len(s2):
            tempStr = s2[r:r+winLen]
            if sorted(s1) == sorted(tempStr):
                return True

            r += 1
        return False
        