from collections import Counter
def generate_pallinromic_permutation(cur_slot,tot_slot,fmap,oddc,asf):
    if cur_slot>tot_slot:
        rev=asf[::-1]
        print(asf+oddc+rev)
        return
    for ch in fmap.keys():
        if fmap[ch]>0:
            fmap[ch]-=1
            generate_pallinromic_permutation(cur_slot+1,tot_slot,fmap,oddc,asf+ch)
            fmap[ch]+=1

str = "aaabb"
fre_dict = dict(Counter(str))
odd_fre_ch=0
odd=""
half_len=0
for ch in fre_dict:
    if fre_dict[ch]%2==1:
        odd=ch
        odd_fre_ch+=1
    half=int(fre_dict[ch]/2)
    fre_dict[ch]=half
    half_len+=half
if odd_fre_ch>1:
    print(-1)
else:
    generate_pallinromic_permutation(1,half_len,fre_dict, odd, "")