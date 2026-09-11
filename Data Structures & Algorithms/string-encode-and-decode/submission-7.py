class Solution:

    def encode(self, strs: List[str]) -> str:
        main_str = ""
        for element in strs:
            main_str += len(element)
            main_str += element
        return main_str

    def decode(self, s: str) -> List[str]:
        print(s)
        return []
