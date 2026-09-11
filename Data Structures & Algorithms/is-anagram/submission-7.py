class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = []
        for element in s:
            chars.append(element)

        print(chars)

        for element in t:
            if element not in chars:
                return False
            else:
                chars.remove(element)
        
        return True