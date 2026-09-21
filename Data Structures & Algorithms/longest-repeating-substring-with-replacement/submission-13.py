class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_dict = {}
        maxlen = 0

        for r in range(len(s)):
            char_dict[s[r]] = 1 + char_dict.get(s[r], 0)

            while (r-l+1) - max(char_dict.values()) > k:
                char_dict[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, r-l+1)
        return maxlen
        
