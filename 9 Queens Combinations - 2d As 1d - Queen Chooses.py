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
        chess[row][col] = True
        queensCombination(qpsf + 1, total_queen, chess, cell)
        chess[row][col] = False

n = int(input("enter size of chess"))
chess = [[False for i in range(n)] for j in range(n)]
queensCombination(0, n, chess, -1)