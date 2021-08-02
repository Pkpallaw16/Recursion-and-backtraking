def dfs(i,n):
    if i>n:
        return
    print(i)
    for j in range(10):
        dfs(10*i+j,n)
def Lexicographical_Numbers(n):
    for i in range(1,10):
        dfs(i,n)

Lexicographical_Numbers(14)