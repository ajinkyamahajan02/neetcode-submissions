class Solution:

    def encode(self, strs: List[str]) -> str:
        main_str = ""
        for element in strs:
            main_str += str(len(element))
            main_str += element

        print(main_str)
        return main_str

    def decode(self, s: str) -> List[str]:
        return []
