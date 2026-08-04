class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """     
        for i in range(len(board)):
            d={}
            for j in range(len(board)):
                if board[i][j].isdigit():
                    if board[i][j] in d:
                        return 1==0
                    else:
                        d[board[i][j]]=1

        for i in range(len(board)):
            d={}
            for j in range(len(board)):
                if board[j][i].isdigit():
                    if board[j][i] in d:
                        return 1==0
                    else:
                        d[board[j][i]]=1
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                d = {}
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c].isdigit():
                            if board[r][c] in d:
                                return False
                            else:
                                d[board[r][c]] = 1
        return 1==1
