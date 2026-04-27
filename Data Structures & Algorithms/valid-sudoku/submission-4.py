import collections 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':
                    continue
                
                elif board[r][c] in rowMap[r] or board[r][c] in colMap[c] or board[r][c] in squares[(r // 3, c // 3)]:

                     return False

                rowMap[r].add(board[r][c])
                colMap[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True

        