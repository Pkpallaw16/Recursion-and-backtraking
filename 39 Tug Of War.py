mindiff=100000
ans=""
def Tug_Of_War(arr,indx,lis1,lis2,sol1,sol2):
    global mindiff,ans
    if indx==len(arr):
        print(lis1,lis2)
        diff=abs(sum(lis1)-sum(lis2))
        if mindiff>diff:
            mindiff=diff
            ans=str(lis1)+" "+str(lis2)
        return

    val=arr[indx]
    if len(lis1)<int((len(arr)+1)/2):
        lis1.append(val)
        Tug_Of_War(arr,indx+1,lis1,lis2,sol1+arr[indx],sol2)
        lis1.pop()
    if len(lis1)>0 and len(lis2)<int((len(arr)+1)/2):
        lis2.append(val)
        Tug_Of_War(arr, indx+1, lis1, lis2, sol1, sol2+arr[indx])
        lis2.pop()

arr=[1,2,3,4,5,6]
Tug_Of_War(arr,0,[],[],0,0)
print(mindiff,ans)