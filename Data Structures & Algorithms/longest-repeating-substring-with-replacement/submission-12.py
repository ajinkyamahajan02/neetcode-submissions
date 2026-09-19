class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        winStart = 0
        winEnd = 0
        maxLen = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            while (r-winStart+1) - max(freq.values()) > k:
                freq[s[winStart]] -= 1
                winStart += 1

            maxLen = max(maxLen, r - winStart + 1)

        return maxLen


            