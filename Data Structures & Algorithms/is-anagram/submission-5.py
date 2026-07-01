from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_c = Counter(s)
        t_c = Counter(t)

        subs = s_c - t_c
        subs2 = t_c - s_c

        if subs or subs2:
            return False

        return True
        