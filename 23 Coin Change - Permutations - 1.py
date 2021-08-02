
def coin_change_permutation(coins,amtsf,tamt,asf,used):
    if amtsf>tamt:
        return
    elif amtsf==tamt:
        print(asf)
        return
    for i in range(len(coins)):
        if used[i]==False:
            used[i]=True
            coin_change_permutation(coins,amtsf+coins[i],tamt,asf+str(coins[i])+"-",used)
            used[i]=False
coins=[2,3,5,6,7]
used=[False for i in range(len(coins))]
coin_change_permutation(coins,0,12,"",used)