class Solution:

    def encode(self, strs: List[str]) -> str:
        main_str = "" 
        for element in strs:
            main_str += str(len(element))
            main_str += "#" + element

        return main_str


    def decode(self, s: str) -> List[str]:
        res = []

        while s:
            for i in range(len(s)):
                if s[i] == "#":
                    break

            length = int(s[0: i])
            res.append(s[i+1: length+i+1])
            s = s[length+i+1:]

        return res