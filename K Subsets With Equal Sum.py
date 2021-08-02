def K_Subsets_With_Equal_Sum(indx,lis,ans,k):
    if indx==len(lis):
        if len(ans)==k:
            flag=True
            for i in range(len(ans)-1):
                if sum(ans[i])!=sum(ans[i+1]):
                    flag=False
            if flag:
                print(ans)
        return
    for p in range(len(ans)):
        ans[p].append(lis[indx])
        K_Subsets_With_Equal_Sum(indx+1,lis,ans,k)
        ans[p].pop()

    if len(ans)+1<=k:
        new_lis=[]
        new_lis.append(lis[indx])
        ans.append(new_lis)
        K_Subsets_With_Equal_Sum(indx + 1, lis, ans, k)
        ans.pop()

lis=[1,2,3,4,5,6]
K_Subsets_With_Equal_Sum(0,lis,[],3)