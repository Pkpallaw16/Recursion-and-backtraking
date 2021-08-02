from collections import Counter
def words_k_selection(str,str_dict,indx,asf,k):
    if k<0:
        return
    if indx==len(str):
        if k==0:
            print(asf)
        return
    ch = str[indx]
    for i in range(str_dict[ch]):
        s=""
        for j in range(i):
            s+=ch
        words_k_selection(str,str_dict,indx+1,asf+s,k-i)

def words_k_selection_2nd(str,str_dict,indx,asf,k):
    if k<0:
        return
    if indx==len(str):
        if k==0:
            print(asf)
        return
    ch = str[indx]
    if str_dict[ch]>0:
        str_dict[ch]-=1
        words_k_selection_2nd(str,str_dict,indx,asf+ch,k-1)
        str_dict[ch]+=1
    words_k_selection_2nd(str, str_dict, indx+1, asf, k )
str="aabbbccdde"
str_dict=dict(Counter(str))
print(str_dict)
#words_k_selection(str,str_dict,0,"",3)
print()
words_k_selection_2nd(str,str_dict,0,"",3)


