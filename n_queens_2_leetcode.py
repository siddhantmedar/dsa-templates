class Solution:

    def totalNQueens(self, n: int) -> int:
        
        def isNotAttacked(n, board, row, col):
            i = row-1
            left = col-1
            right  = col+1

            while i>=0:
                if board[i][col] == 'Q' \
                or (left>=0 and board[i][left] == 'Q') \
                or(right < n and board[i][right] == 'Q'):
                    return False
                else:
                    i-=1
                    left-=1
                    right+=1

            return True
        
        def solveNQueensRec(n, board, row):
            if row>=n:
                return 1
            
            ways = 0
            
            for i in range(n):
                if isNotAttacked(n, board, row, i):
                    board[row][i] = 'Q'
                    ways+=solveNQueensRec(n, board, row+1)
                    board[row][i] = '.'

            return ways

        board = [["."]*n for i in range(n)]
        return solveNQueensRec(n, board, 0)