class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_dict = {}
        maxlen = 0

        for r in range(len(s)):
            char_dict[s[r]] = 1 + char_dict.get(s[r], 0)
            if min(char_dict.values()) <= k or len(char_dict) <= 1:
                maxlen = max(maxlen, r - l + 1)
            else:
                if char_dict.get(s[l]) == 1:
                    char_dict.pop(s[l])
                else:
                    char_dict[s[l]] = char_dict.get(s[l]) - 1
                    l += 1

                maxlen = max(maxlen, r - l + 1)

        return maxlen
