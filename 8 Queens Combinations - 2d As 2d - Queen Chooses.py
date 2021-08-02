def queenscombinations(qpsf,total_queen,chess,prev_placed_qn_row,prev_placed_qn_col):
    if qpsf==total_queen:
        for row in range(len(chess)):
            for col in range(len(chess[0])):
                if chess[row][col]==True:
                    print("q\t",end="")
                else:
                    print("-\t",end="")
            print()
        print()
    for col in range(prev_placed_qn_col+1,len(chess)):
        chess[prev_placed_qn_row][col]=True
        queenscombinations(qpsf+1,total_queen,chess,prev_placed_qn_row,col)
        chess[prev_placed_qn_row][col]=False

    for row in range(prev_placed_qn_row + 1, len(chess)):
        for col in range(len(chess)):
            chess[row][col] = True
            queenscombinations(qpsf + 1, total_queen, chess, row, col)
            chess[row][col] = False


n=int(input("enter chess size"))
chess=[[False for i in range(n)] for j in range(n)]
queenscombinations(0,n,chess,0,-1)