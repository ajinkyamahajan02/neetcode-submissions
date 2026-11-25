class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = ""

        def dfs(openB, closeB, subset):
            if openB == n and closeB == n:
                res.append(subset)
                return 

            if openB < n:
                    dfs(openB+1, closeB, subset+"(")
            if closeB < openB:
                dfs(openB, closeB+1, subset+")")

        dfs(0, 0, "")
        return res



