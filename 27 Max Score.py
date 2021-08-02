
value_sore=["1", "0", "9", "5", "0", "0", "3", "0", "0", "0", "0", "0", "0", "0", "2", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0"]
def check_word_in_limit_of_freq(word,fre_count):
    flag=True
    for ch in word:
        index=ord(ch)-ord("a")
        if fre_count[index]<=0:
            flag=False
        fre_count[index]-=1
    return flag
def reset_freq(word,fre_count):
    for ch in word:
        index=ord(ch)-ord("a")
        fre_count[index]+=1
def calculate_score(word):
    global value_sore
    score=0
    for ch in word:
        score+=int(value_sore[ord(ch)-ord("a")])
    return score
def max_score(words,fre_count,index):
    if index==len(words):
        return 0
    max_sco=0
    max_sco = max(max_sco, max_score(words, fre_count, index + 1))
    if check_word_in_limit_of_freq(words[index], fre_count):
        max_sco=max(max_sco,max_score(words,fre_count,index+1)+calculate_score(words[index]))
    reset_freq(words[index],fre_count)
    return max_sco
def freq_count(freq):
    fre_count=[0 for i in range(26)]
    for ch in freq:
        fre_count[ord(ch)-ord("a")]+=1
    return fre_count
word_num=4
words=["dog", "cat", "dad", "good",]
freq_len=9
freq=["a", "b", "c", "d", "d", "d", "g", "o", "o"]
fre_count=freq_count(freq)
print(fre_count)
print(max_score(words,fre_count,0))