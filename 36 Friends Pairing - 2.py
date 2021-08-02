count=1
def friends_pairing_combination(i,n,used,asf):
    global count
    if i>n:
        print(count,asf)
        count+=1
        return
    if used[i]==True:
        friends_pairing_combination(i+1,n,used,asf)
    else:
        used[i]=True
        friends_pairing_combination(i+1,n,used,asf+"("+str(i)+")")
        for j in range(i+1,n+1):
            if used[j]==False:
                used[j]=True
                friends_pairing_combination(i+1,n,used,asf+"("+str(i)+","+str(j)+")")
                used[j]=False
        used[i]=False

n=3
used=[False for i in range(n+1)]
friends_pairing_combination(1,n,used,"")