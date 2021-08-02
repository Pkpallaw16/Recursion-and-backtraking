def isItsSafePlaceForThequeen(chess, row,col):
    ndir=[0,-1,-1,-1,0,1,1,1]
    cdir=[-1,-1,0,1,1,1,0,-1]
    for i in range(1,len(chess)):
        for index in range(len(ndir)):
            nrow=row+ndir[index] *i
            ncol=col+cdir[index] *i
            #print(nrow,ncol)
            if nrow>=0 and ncol>=0 and nrow<len(chess) and ncol<len(chess) and chess[nrow][ncol] != 0:
                return False
    return True

def Nqueenspermutations(qpsf, total_queen, chess):
    if qpsf == total_queen:
        for row in range(len(chess)):
            for col in range(len(chess)):
                if chess[row][col]:
                    print("q"+str(chess[row][col])+"\t", end="")
                else:
                    print("-\t", end="")
            print()
        print()
        return

    for cell in range(len(chess) * len(chess)):
        row = int(cell / len(chess))
        col = cell % len(chess)
        if chess[row][col] == 0 and isItsSafePlaceForThequeen(chess, row,col):
            chess[row][col] = qpsf+1
            Nqueenspermutations(qpsf + 1, total_queen, chess)
            chess[row][col] = 0

n = 4 #int(input("enter size of chess"))
chess = [[False for i in range(n)] for j in range(n)]
Nqueenspermutations(0, n, chess)