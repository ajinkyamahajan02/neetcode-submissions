class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(n):
            
            singles = ""
            if n == 1:
                res.append(subset)
                res.append(singles)
                return
            
            subset.insert(0, "(")
            subset.insert(-1, ")")
            singles.append("()")
            dfs(n-1)

        dfs(n)
        print(res)
        return res