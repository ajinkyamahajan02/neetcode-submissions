class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(idx, subset):
            if idx >= len(s):
                res.append(subset.copy())
                return 

            for j in range(idx, len(s)):
                if s[idx: j+1] == s[idx:j+1][::-1]:
                    subset.append(s[idx:j+1])
                    dfs(j+1, subset)
                    subset.pop()
        dfs(0, [])
        return res
