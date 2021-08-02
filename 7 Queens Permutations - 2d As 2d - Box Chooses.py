def queensPermutations(qpsf,total_queen,row,col,asf,queens):
    if row==total_queen:
        if qpsf==total_queen:
            print(asf)
            print()
        return

    nr=0
    nc=0
    sep=""
    if col==total_queen-1:
        nr=row+1
        nc=0
        sep="\n"
    else:
        nr=row
        nc=col+1
        sep="\t"
    for i in range(len(queens)):
        if queens[i]==False:
            queens[i]=True
            queensPermutations(qpsf+1,total_queen,nr,nc,asf+"q"+str(i+1)+sep,queens)
            queens[i]=False
    queensPermutations(qpsf, total_queen, nr, nc, asf + "-" + sep, queens)


n=int(input("enter chess size"))
queens=[False for i in range(n)]
queensPermutations(0,n,0,0,"",queens)