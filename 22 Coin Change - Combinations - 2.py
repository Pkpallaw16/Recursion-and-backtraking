
def coin_change_combination(indx,coins,amtsf,tamt,asf):
    if indx==len(coins):
        if amtsf==tamt:
            print(asf)
        return
    for j in range(int((tamt-amtsf)/2),0,-1):
        part=""
        for k in range(j):
            part+=str(coins[indx])+"-"
        coin_change_combination(indx+1,coins,amtsf+(coins[indx]*j),tamt,asf+part)
    coin_change_combination(indx + 1, coins, amtsf, tamt, asf)
coins=[2,3,5,6,7]
coin_change_combination(0,coins,0,12,"")