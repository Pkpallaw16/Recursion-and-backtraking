def is_safe(goldmine,r,c):
    if r>=0 and c>=0 and r<len(goldmine) and c<len(goldmine) and goldmine[r][c]>0:
        return True
    else:
        return False
def maximum_amount_of_gold_dfs(goldmine,i,j):
    row = [-1, 0, 1, 0]
    col = [0, 1, 0, -1]
    gold=goldmine[i][j]
    goldmine[i][j] *=-1
    for opt in range(len(row)):
        if is_safe(goldmine ,i + row[opt], j + col[opt]):
            gold+=maximum_amount_of_gold_dfs(goldmine, i + row[opt], j + col[opt])
    return gold
row=int(input("enter number of row: "))
col=int(input("enter number of col: "))
goldmine=[[int(x) for x in input().split()] for i in range(row)]
max1=0
for i in range(col):
    for j in range(row):
        if goldmine[i][j]>0:
            res=maximum_amount_of_gold_dfs(goldmine,i,j)
            max1=max(max1,res)
#Tabulation
print(max1)