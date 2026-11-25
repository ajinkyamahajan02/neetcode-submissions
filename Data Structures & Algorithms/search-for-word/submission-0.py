class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        
        def dfs(r, c, index):
            if index == len(word):
                return True

            if (r < 0 or 
                c < 0 or 
                r > len(board) or 
                c > len(board[0]) or 
                (r,c) in path or
                word[index] != board[r][c]):
                return False
            
            path.add((r,c))

            res = ( dfs(r+1, c, index+1) or
                    dfs(r-1, c, index+1) or
                    dfs(r, c+1, index+1) or
                    dfs(r, c-1, index+1))
            path.remove((r,c))
            return res
            
        for r in range(len(board)):
            for c in range(len(board[r])):
                if dfs(r,c,0):
                    return True 
        return False