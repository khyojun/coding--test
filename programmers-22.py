def solution(d, budget): # 예산
    answer = 0
    maxi=0
    d.sort()
    tmp=0
    for i in range(1, len(d)+1):
        tmp=sum(d[0:i])
        if tmp>budget:
            return i-1
        elif tmp==budget:
            return i
    
    if tmp<budget:
        return len(d)
    return answer