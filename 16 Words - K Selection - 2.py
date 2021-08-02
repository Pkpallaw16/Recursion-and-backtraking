"""1. You are given a word (may have one character repeat more than once).
2. You are given an integer k.
2. You are required to generate and print all ways you can select k distinct characters out of the
     word."""
def words_k_selection(uniqu_str,indx,k,sel_str,last_box):
    if indx==k:
        print(sel_str)
        return
    for i in range(last_box+1,len(uniqu_str)):
        ch=uniqu_str[i]
        words_k_selection(uniqu_str, indx+1, k, sel_str+ch,i)
str="aabbbccdde"
k=3
s=set()
uniqu_str=""
for ch in str:
    if ch not in s:
        s.add(ch)
        uniqu_str+=ch

words_k_selection(uniqu_str,0,k,"",-1)