"""1. You are given a word (may have one character repeat more than once).
2. You are given an integer k.
2. You are required to generate and print all ways you can select k distinct characters out of the
     word."""
def words_k_selection(str,indx,asf,k):
    if indx==len(str):
        if len(asf)==k:
            print(asf)
        return
    words_k_selection(str,indx+1,asf+str[indx],k)
    words_k_selection(str, indx+1, asf,k)
str="aabbbccdde"
k=3
s=set()
uniqu_str=""
for ch in str:
    if ch not in s:
        s.add(ch)
        uniqu_str+=ch
words_k_selection(uniqu_str,0,"",k)
