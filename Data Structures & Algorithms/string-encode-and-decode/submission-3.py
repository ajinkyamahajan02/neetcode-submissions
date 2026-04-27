class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for element in strs:
            encoded_word = str(len(element)) + "#" + str(element)
            encoded_str += encoded_word

        print(encoded_str)
        return encoded_str


    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        final_lst = []

        for c in s:
            if c == "#" and s:
                if s[(s.index("#"))-1].isdigit():
                    word_length = int(s[0:s.index("#")])

                    length = len(str(word_length))
                    if length == 1:
                        word = s[2:word_length+2]
                        s = s[word_length+2:]

                    elif length == 2:
                        word = s[3:word_length+3]
                        s = s[word_length+3:]

                    elif length == 3:
                        word = s[4:word_length+4]
                        s = s[word_length+4:]

                    final_lst.append(word)

        return final_lst