class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openB, closedB, subset):
            if openB == n and closedB == n:
                res.append(subset)
                return 

            if openB < n:
                dfs(openB+1, closedB, subset+"(") 
            if closedB < openB:
                dfs(openB, closedB+1, subset+")")

        dfs(0,0,"")
        return res

            
        