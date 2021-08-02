def queensPermutations(qpsf,total_queen,chess):
    if qpsf==total_queen:
        for i in range(len(chess)):
            for j in range(len(chess[0])):
                if chess[i][j] == 0:
                    print("-\t",end="")
                else:
                    print("q"+str(chess[i][j])+"\t",end="")
            print()
    for i in range(len(chess)):
        for j in range(len(chess[0])):
            if chess[i][j]==0:
                chess[i][j]=qpsf+1
                queensPermutations(qpsf+1,total_queen,chess)
                chess[i][j]=0

n=int(input("enter chess size"))
chess=[[0 for i in range(n)] for j in range(n)]
queensPermutations(0,n,chess)

