class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        winStart = 0
        winEnd = 0
        maxLen = 0

        while winEnd < len(s):
            tempChar = s[winEnd]
            freq[tempChar] = freq.get(tempChar, 0) + 1
            
                
            if ((winEnd - winStart + 1) - max(freq.values())) > k:
                tempChar = s[winStart]
                freq[tempChar] = freq.get(tempChar) - 1
                winStart += 1

            maxLen = max(maxLen, (winEnd - winStart + 1))
            winEnd += 1

        return maxLen
