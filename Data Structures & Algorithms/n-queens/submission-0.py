class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        posD = set()
        negD = set()
        col = set()

        def dfs(r):
            if r == n:
                t = ["".join(row) for row in board]
                res.append(t)
                return 
            
            for c in range(n):
                if ((r+c) in posD or 
                    (r-c) in negD or 
                    c in col):
                    continue
                
                posD.add(r+c)
                negD.add(r-c)
                col.add(c)
                board[r][c] = "Q"

                dfs(r+1)

                posD.remove(r+c)
                negD.remove(r-c)
                col.remove(c)
                board[r][c] = "."
        dfs(0)
        return res