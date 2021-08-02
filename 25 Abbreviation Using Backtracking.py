def Abbreviation_Using_Backtracking(str1,asf,count,indx):
    if indx==len(str1):
        if count==0:
            print(asf)
        else:
            print(asf+str(count))
        return
    if count>0:
        Abbreviation_Using_Backtracking(str1,asf+str(count)+str1[indx],0,indx+1)
    else:
        Abbreviation_Using_Backtracking(str1, asf + str1[indx], 0, indx + 1)
    Abbreviation_Using_Backtracking(str1,asf,count+1,indx+1)

Abbreviation_Using_Backtracking("pep","",0,0)