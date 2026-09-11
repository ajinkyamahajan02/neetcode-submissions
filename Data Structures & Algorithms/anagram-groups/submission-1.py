class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for element in strs:
            sorted_word = sorted(strs)
            if sorted_word in list(words.keys()):
                current = words.get(sorted_word)
                current.append(element)
                words[sorted_word] = current
            else:
                print(sorted_word)
                words[sorted_word] = [element]

        res = []
        res.extend(words.values())
        return res

