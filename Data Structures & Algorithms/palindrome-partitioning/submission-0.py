class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(idx):
            if idx >= len(s):
                res.append(part.copy())
                return 
            
            for j in range(idx, len(s)):
                if s[idx:j+1] == s[idx:j+1][::-1]:
                    part.append(s[idx:j+1])
                    dfs(j+1)
                    part.pop()
            
        dfs(0)
        return res