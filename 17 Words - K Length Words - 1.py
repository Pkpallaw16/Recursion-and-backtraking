"""1. You are given a word (may have one character repeat more than once).
2. You are given an integer k.
3. You are required to generate and print all k length words (of distinct chars) by using chars of the
     word."""
from collections import Counter
# number of boxes is less compared to number of string
def Word_k_length_words(ustr,k,box_level,asf,spots):
    if box_level==k:
        if len(asf)==k:
            print(asf)
        return
    for i in range(len(spots)):
        if spots[i]==None:
            spots[i]=ustr[i]
            Word_k_length_words(ustr,k,box_level+1,asf+ustr[i],spots)
            spots[i]=None
    Word_k_length_words(ustr, k, box_level + 1, asf,spots)

str="aabbbccdde"
str_dict=dict(Counter(str))
ustr=""
for ch in str_dict:
    ustr=ustr+ch
spots=[None for i in range(len(ustr))]
Word_k_length_words(ustr,3,0,"",spots)