
s="aabbaccc"
answer = 1000
cnt=1
answer_s=""
for cut in range(1,len(s)): 
    tmp=s[:cut]
    for j in range(cut, len(s)+3, cut):     
        if tmp == s[j:j+cut]:
            cnt+=1
        else:
            if cnt==1:
                answer_s=answer_s+tmp
            else:
                answer_s=answer_s+str(cnt)+tmp
            tmp=s[j:j+cut]
            cnt=1
    answer=min(len(answer_s), answer)
    answer_s=""
     
print(answer)