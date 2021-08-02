"""1. You are given a word (may have one character repeat more than once).
2. You are given an integer k.
3. You are required to generate and print all k length words (of distinct chars) by using chars of the
     word."""
from collections import Counter
def permutations(ustr,vis,cs,ts,asf):
    if cs>ts:
        print(asf)
        return
    for i in range(len(ustr)):
        ch=ustr[i]
        if ch not in vis:
            vis.add(ch)
            permutations(ustr,vis,cs+1,ts,asf+ch)
            vis.remove(ch)

str="aabbbccdde"
str_dict=dict(Counter(str))
ustr=""
for ch in str_dict:
    ustr=ustr+ch
print(ustr)
permutations(ustr,set(),1,3,"")


