def isPallindrome(prefix):
    lch=0
    rch=len(prefix)-1
    while lch<rch:
        if prefix[lch]!=prefix[rch]:
            return False
        lch+=1
        rch-=1
    return True
def All_Palindromic_Partitions(str1,asf):
    if len(str1)==0:
        print(asf)
        return
    for i in range(len(str1)):
        prefix=str1[:i+1]
        ros=str1[i+1:]
        if isPallindrome(prefix):
            All_Palindromic_Partitions(ros,asf+"("+prefix+")")



str1="abaaba"
All_Palindromic_Partitions(str1,"")