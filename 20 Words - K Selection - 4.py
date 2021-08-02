from collections import Counter
def words_k_selection(unique_str,str_dict,cur_spot,tot_spot,asf,last_index):
    if cur_spot==tot_spot:
        print(asf)
        return
    for i in range(last_index,len(unique_str)):
        ch=unique_str[i]
        if str_dict[ch]>0:
            str_dict[ch]-=1
            words_k_selection(unique_str,str_dict,cur_spot+1,tot_spot,asf+ch,i)
            str_dict[ch]+=1
str="aabbbccdde"
str_dict=dict(Counter(str))
print(str_dict)
unique_str=("").join(str_dict.keys())
#words_k_selection(str,str_dict,0,"",3)
print(unique_str)
k=3
words_k_selection(unique_str,str_dict,0,k,"",0)