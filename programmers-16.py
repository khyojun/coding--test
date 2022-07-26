def solution(n, lost, reserve): # 체육복
    answer = 0
    answer=n
    answer-=len(lost)
    lost.sort()
    reserve.sort()
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i]=0
            answer+=1
    
    for i in range(0,len(lost)):
        if lost[i]==0:
            continue
        
        for j in range(0, len(reserve)):
            if abs(lost[i]-reserve[j])==1:
                del reserve[j]
                answer+=1
                break
    
    
    return answer