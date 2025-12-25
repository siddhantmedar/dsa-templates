class Solution:        
        def solveNQueens(self, n: int) -> List[List[str]]:
            def isNotAttacked(n, board, row, col):
                i = row-1
                left = col-1
                right  = col+1

                while i>=0:
                    if board[i][col] == 'Q' or (left>=0 and board[i][left] == 'Q') or(right < n and board[i][right] == 'Q'):
                        return False
                    else:
                        i-=1
                        left-=1
                        right+=1
                return True

            def create_board(board):
                lst = []
                for rows in board:
                    lst.append("".join(rows))
                return lst

            def solveNQueensRec(n, board, row):
                if row>=n:
                    board_state.append(create_board(copy.deepcopy(board)))
                    return

                for i in range(n):
                    if isNotAttacked(n, board, row, i):
                        board[row][i] = 'Q'
                        solveNQueensRec(n, board, row+1)
                        board[row][i] = '.'


            board_state = []
            board = [["."]*n for i in range(n)]
            solveNQueensRec(n, board, 0)
            return board_state   