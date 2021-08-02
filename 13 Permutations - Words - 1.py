"""1. You are given a word (may have one character repeat more than once).
2. You are required to generate and print all arrangements of these characters. """
from collections import Counter
#boxes on level letters on options
def PermutationsWords(cur_lev,tot_lev,fmap,asf):
    if cur_lev>tot_lev:
        print(asf)
        return 

    for uni_let in fmap.keys():
        if fmap[uni_let]>0:
            fmap[uni_let]-=1
            PermutationsWords(cur_lev+1,tot_lev,fmap,asf+uni_let)
            fmap[uni_let] += 1


str="aabb"
fmap=dict(Counter(str))
print(fmap)
PermutationsWords(1,len(str),fmap,"")