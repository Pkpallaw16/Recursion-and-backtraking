
def IntegerFromMap(s1,charmap):
    num=0
    for s in s1:
        num=(num*10)+charmap[s]
    return num
def Cryptarithmetic(unique,idx,charmap,usednum,s1,s2,s3):
    if idx==len(unique):
        n1=IntegerFromMap(s1,charmap)
        n2=IntegerFromMap(s2,charmap)
        n3=IntegerFromMap(s3,charmap)
        if n1+n2==n3:
            for i in range(26):
                ch=chr(i+ord("a"))
                if ch in charmap:
                    print("{},-{}".format(ch,charmap[ch]),end=" ")
            print()
        return
    for i in range(10):
        if usednum[i]==False:
            charmap[unique[idx]]=i
            usednum[i] = True
            Cryptarithmetic(unique,idx+1,charmap,usednum,s1,s2,s3)
            usednum[i]=False
            del charmap[unique[idx]]
s1="team"
s2="pep"
s3="toppr"
charmap={}
usednum=[False for i in range(10)]
str=s1+s2+s3
unique=""
for s in str:
    if s not in unique:
        unique=unique+s
print(unique)
Cryptarithmetic(unique,0,charmap,usednum,s1,s2,s3)