def isSafeToPalceNum(board,row,col,num):
    for c in range(len(board[0])):
        if board[row][c]==num:
            return False
    for r in range(len(board)):
        if board[r][col]==num:
            return False
    rr=row-(row%3)
    cc=col-(col%3)
    for i in range(3):
        for j in range(3):
            if board[i+rr][j+cc]==num:
                return False
    return True

def solve_suduku(board,i,j):
    if i==len(board):
        print(board)
        return
    if board[i][j]==0:
        for num in range(1,10):
            if isSafeToPalceNum(board,i,j,num):
                #place
                board[i][j]=num
                if j==len(board[0])-1:
                    solve_suduku(board,i+1,0)
                else:
                    solve_suduku(board,i,j+1)
                #unplace
                board[i][j]=0
    else:
        if j == len(board[0]) - 1:
            solve_suduku(board, i + 1, 0)
        else:
            solve_suduku(board, i, j + 1)

print("Enter Sudoku: ")
board=[[int(x) for x in input().split()] for i in range(9)]
solve_suduku(board,0,0)