count=1
def K_partition_list(i,n,k,ans):
    global count
    if i>n:
        if len(ans)==k:
            print(count,".",end=" ")
            for i in range(len(ans)):
                print(ans[i],end=" ")
            print()
            count+=1
        return
    #n-1,k work add with previous option
    for j in range(len(ans)):
        lis=ans[j]
        lis.append(i)
        K_partition_list(i+1,n,k,ans)
        lis.pop(len(ans)-1)
    #n-1,k-1 work, add with previous options
    if len(ans)+1<=k:
        mres=[]
        mres.append(i)
        ans.append(mres)
        K_partition_list(i + 1, n, k,ans)
        ans.pop(len(ans)-1)
n=int(input("Enter value of n: "))
k=int(input("Enter value of k: "))
K_partition_list(1,n,k,[])