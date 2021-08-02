def NQueens_Branch_And_Bound(board,row,cols,ndiag,rdiag,asf):
    if row==len(board):
        print(asf)
        return
    for col in range(len(board[0])):
        if cols[col]==False and ndiag[row+col]==False and rdiag[row-col+len(board)-1]==False:
            board[row][col]=True
            cols[col] = True
            ndiag[row + col] = True
            rdiag[row - col + len(board) - 1] =True
            NQueens_Branch_And_Bound(board,row+1,cols,ndiag,rdiag,asf+str(row)+"-"+str(col)+"-")
            board[row][col] = False
            cols[col] =False
            ndiag[row + col] = False
            rdiag[row - col + len(board) - 1] = False

n=4
board=[[0 for i in range(n)] for j in range(n)]
cols=[False for i in range(n)]
ndiag=[False for i in range(2*n-1)]
rdiag=[False for i in range(2*n-1)]
NQueens_Branch_And_Bound(board,0,cols,ndiag,rdiag,"")