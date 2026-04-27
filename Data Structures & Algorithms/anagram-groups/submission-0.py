class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        lookup = {}

        for single_str in strs:
            sorted_str = "".join(sorted(single_str))

            if sorted_str in lookup.keys():
                lookup[sorted_str].append(single_str)

            else:
                lookup[sorted_str]= [single_str]

        lst = []
        for element in lookup.values():
            lst.append(element)

        return lst