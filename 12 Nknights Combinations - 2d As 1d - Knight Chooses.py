def isItsSafePlaceForTheKnight(chess, row,col):
    ndir=[-2,-1,-1,-2]
    cdir=[1,2,-2,-1]

    for i in range(len(ndir)):
        nrow=row+ndir[i]
        ncol=col+cdir[i]
        #print(nrow,ncol)
        if nrow>=0 and ncol>=0 and nrow<len(chess) and ncol<len(chess) and chess[nrow][ncol] == True:
            return False
    return True

def NKnightsCombination(qpsf, total_queen, chess, last_cell_no):
    if qpsf == total_queen:
        for row in range(len(chess)):
            for col in range(len(chess)):
                if chess[row][col]:
                    print("k\t", end="")
                else:
                    print("-\t", end="")
            print()
        print()
        return

    for cell in range(last_cell_no+1, len(chess) * len(chess)):
        row = int(cell / len(chess))
        col = cell % len(chess)
        if chess[row][col] == False and isItsSafePlaceForTheKnight(chess, row,col):
            chess[row][col] = True
            NKnightsCombination(qpsf + 1, total_queen, chess, cell)
            chess[row][col] = False

n = 4 #int(input("enter size of chess"))
chess = [[False for i in range(n)] for j in range(n)]
NKnightsCombination(0, n, chess, -1)