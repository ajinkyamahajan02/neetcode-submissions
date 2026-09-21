from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def is_subset(subset, superset):
            return subset.items() <= superset.items() 

        t_map = Counter(t)
        tempDict = {}
        l = r = 0
        winStart = -1
        winEnd = -1
        minWin = float("infinity")

        while r < len(s):
            tempDict[s[r]] = 1 + tempDict.get(s[r], 0)
            while is_subset(t_map, tempDict):
                if minWin > r - l + 1:
                    winStart = l
                    winEnd = r
                    minWin = r - l + 1
                if tempDict.get(s[l]) == 1:
                    tempDict.pop(s[l])
                else:
                    tempDict[s[l]] -= 1
                l += 1
            r += 1

        if winEnd == -1 and winStart == -1:
            return ""
        return s[winStart:winEnd+1]         


