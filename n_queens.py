n=4
board_state = []

def isNotAttacked(board, row, col):
    i = row-1
    left = col-1
    right = col+1

    while i>=0:
        if board[i][col] == "Q" or (left>=0 and board[i][left] == "Q") or (right < n and board[i][right] == "Q"):
            return False
        else:
            i-=1
            left-=1
            right+=1

    return True

def NQueensRec(n, board, row):
    if row >= n:
        board_state.append(board)
        return 1
    
    ways = 0

    for i in range(n):
        if isNotAttacked(board, row, i):
            board[row][i] = "Q"
            ways+= NQueensRec(n, board, row+1)
            board[row][i] = "."

    return ways

def NQueens(n):
    board = [['.'] for i in range(n)]
    print(NQueensRec(n, board, 0))
    print(board_state)

NQueens(n)