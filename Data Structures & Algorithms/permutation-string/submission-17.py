class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sw = len(s1)

        for i in range(0, len(s2)):
            tempStr = s2[i: i+sw]
            if sorted(tempStr) == sorted(s1):
                return True


        return False