
"""1. You are given a word (may have one character repeat more than once).
2. You are required to generate and print all arrangements of these characters. """
#letters on option and boxes on option
def permutation_words(str,indx,index_map,boxes):
    if indx==len(str):
        print(("").join(boxes))
        return
    ch = str[indx]
    lo=index_map[ch]
    for i in range(lo+1,len(boxes)):
        if boxes[i]==None:
            index_map[ch]=i
            boxes[i]=ch
            permutation_words(str,indx+1,index_map,boxes)
            index_map[ch]=lo
            boxes[i] =None

str="aabb"
index_map={}
for ch in str:
    if ch not in index_map:
        index_map[ch]=-1
boxes=[None for i in range(len(str))]
print(index_map)
permutation_words(str,0,index_map,boxes)


