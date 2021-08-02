def isItsSafePlaceForThequeen(chess, row,col):
    ndir=[-1,-1,-1]
    cdir=[0,-1,1]
    for c in range(col):
        if chess[row][c]==True:
            return False
    for i in range(1,row+1):
        for index in range(len(ndir)):
            nrow=row+ndir[index] *i
            ncol=col+cdir[index] *i
            #print(nrow,ncol)
            if nrow>=0 and ncol>=0 and nrow<len(chess) and ncol<len(chess) and chess[nrow][ncol] == True:
                return False
    return True

def queensCombination(qpsf, total_queen, chess, last_cell_no):
    if qpsf == total_queen:
        for row in range(len(chess)):
            for col in range(len(chess)):
                if chess[row][col]:
                    print("q\t", end="")
                else:
                    print("-\t", end="")
            print()
        print()
        return

    for cell in range(last_cell_no+1, len(chess) * len(chess)):
        row = int(cell / len(chess))
        col = cell % len(chess)
        if isItsSafePlaceForThequeen(chess, row,col):
            chess[row][col] = True
            queensCombination(qpsf + 1, total_queen, chess, cell)
            chess[row][col] = False

n = 4 #int(input("enter size of chess"))
chess = [[False for i in range(n)] for j in range(n)]
queensCombination(0, n, chess, -1)