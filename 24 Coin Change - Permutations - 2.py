
def coin_change_permutation(coins,amtsf,tamt,asf):
    if amtsf>tamt:
        return
    elif amtsf==tamt:
        print(asf)
        return
    for i in range(len(coins)):
        coin_change_permutation(coins,amtsf+coins[i],tamt,asf+str(coins[i])+"-")

coins=[2,3,5,6,7]
coin_change_permutation(coins,0,12,"")