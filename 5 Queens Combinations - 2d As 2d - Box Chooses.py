def queensCombinations(qpsf,total_queen,row,col,asf):
    if row ==total_queen:
        if qpsf==total_queen:
            print(asf)
        return
    nr=0
    nc=0
    yasf=""
    nasf=""
    if col==total_queen-1:
        nr=row+1
        nc=0
        yasf=asf+"q\n"
        nasf=asf+"-\n"
    else:
        nr=row
        nc=col+1
        yasf = asf + "q"
        nasf = asf + "-"

    queensCombinations(qpsf+1,total_queen,nr,nc,yasf)
    queensCombinations(qpsf, total_queen, nr, nc, nasf)
n=int(input("enter chess size"))
queensCombinations(0,n,0,0,"")