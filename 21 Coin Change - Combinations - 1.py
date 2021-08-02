
def coin_change_combination(indx,coins,amtsf,tamt,asf):
    if indx==len(coins):
        if amtsf==tamt:
            print(asf)
        return
    coin_change_combination(indx+1,coins,amtsf+coins[indx],tamt,asf+str(coins[indx])+"-")
    coin_change_combination(indx + 1, coins, amtsf, tamt, asf)
coins=[2,3,5,6,7]
coin_change_combination(0,coins,0,12,"")