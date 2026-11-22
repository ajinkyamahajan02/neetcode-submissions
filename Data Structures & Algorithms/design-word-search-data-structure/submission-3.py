class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True
        
    def search(self, word: str) -> bool:

        def dfs(i, curr):
            
            for index in range(i, len(word)):
                c = word[index]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(index + 1, child):
                            return True
                        return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.is_end

        return dfs(0, self.root)