def Crossword(grid,words,index):
    if index==len(words):
        for row in grid:
            print(row)
        return
    word=words[index]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="-" or grid[i][j]==word[0]:
                #horizontal try
                if CanPalceHorizontal(grid,i,j,word):
                    status=PalceHorizontal(grid,i,j,word)
                    Crossword(grid, words, index+1)
                    UnPalceHorizontal(grid, i, j, status)
                if CanPalceVertical(grid,i,j,word):
                    status=PalceVertical(grid,i,j,word)
                    Crossword(grid, words, index+1)
                    UnPalceVertical(grid,i,j,status)
def CanPalceHorizontal(grid,r,c,word):
    #left check
    if c-1>=0 and grid[r][c-1]!="+":
        return False
    #right check
    elif (c+len(word)<len(grid[0])) and (grid[r][c+len(word)]!="+"):
        return False
    l=len(word)
    for i in range(l):
        if c+i>=len(grid[0]):
            return False
        if grid[r][c+i]!="-" and grid[r][c+i]!=word[i]:
            return False
    return True
def PalceHorizontal(grid, r, c, word):
    status=[False for i in range(len(word))]
    for j in range(len(word)):
        if grid[r][c+j]=="-":
            grid[r][c+j]=word[j]
            status[j]=True
    return status
def UnPalceHorizontal(grid, r, c, status):
    for j in range(len(status)):
        if status[j]==True:
            grid[r][c+j]="-"
    return
def CanPalceVertical(grid, r, c, word):
    if r-1>=0 and grid[r-1][c]!="+":
        return False
    elif (r+len(word)<len(grid)) and (grid[r+len(word)][c]!="+"):
        return False
    for j in range(len(word)):
        if r+j>=len(grid):
            return False
        if grid[r+j][c]!="-" and grid[r+j][c]!=word[j]:
            return False
    return True
def PalceVertical(grid, r, c, word):
    status = [False for i in range(len(word))]
    for j in range(len(word)):
        if grid[r + j][c] == "-":
            grid[r + j][c] = word[j]
            status[j]=True
    return status
def UnPalceVertical(grid,r, c, status):
    for j in range(len(status)):
        if status[j]==True:
            grid[r+j][c]="-"
    return

def fun():
    grid=[['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'], ['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'], ['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'], ['+', '-', '-', '-', '-', '-', '+', '+', '+', '+'], ['+', '-', '+', '+', '+', '-', '+', '+', '+', '+'], ['+', '-', '+', '+', '+', '-', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '-', '+', '+', '+', '+'], ['+', '+', '-', '-', '-', '-', '-', '-', '+', '+'], ['+', '+', '+', '+', '+', '-', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '-', '+', '+', '+', '+']]
    words=['LONDON', 'DELHI', 'ICELAND', 'ANKARA']
    Crossword(grid,words,0)
fun()


