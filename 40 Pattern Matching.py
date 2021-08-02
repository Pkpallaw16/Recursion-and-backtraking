def Pattern_Matching(str1,pattern,map_dic,indx,asf):
    if indx==len(pattern):
        if len(str1)==0:
            print(asf)
        return

    ch=pattern[indx]
    mapping=map_dic[ch]
    for i in range(len(str1)):
        substr=str1[:i+1]
        roq=str1[i+1:]
        map_dic[ch]=substr
        if len(mapping)>0:
            if substr.equals(mapping)==True:
                Pattern_Matching(roq,pattern,map_dic,indx+1)
        else:
            Pattern_Matching(roq, pattern, map_dic, asf + ch + "->" + substr + ",", indx + 1)
        map_dic[ch]=mapping