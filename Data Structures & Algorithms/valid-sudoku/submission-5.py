class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            element_set = set()
            for element in row:
                if element in element_set:
                    return False
                else:
                    if element != '.':
                        element_set.add(element)

        for i in range(len(board[0])):
            element_set = set()
            for j in range(len(board)):
                if board[j][i] in element_set:
                    return False
                else:
                    if board[j][i] != '.':
                        element_set.add(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                element_set = set()
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if board[r][c] in element_set:
                            return False
                        else:
                            if board[r][c] != '.':
                                element_set.add(board[r][c])


        return True
