def solution(dartResult): # 다트게임
    answer = 0
    now=0
    before=0
    star=0
    flag=0
    for i in range(0, len(dartResult)):
        if dartResult[i:i+2]=='10':
            if star==1:
                answer+=before+now*2
                before=now*2
            else:
                answer+=now
                before=now
            star=0
            now=10
            flag=1
            continue
        elif dartResult[i]>='0' and dartResult[i]<='9':
            if flag==1:
                flag=0
                continue
            if star==1:
                answer+=before+now*2
                before=now*2
            else:
                answer+=now
                before=now
            star=0
            now=int(dartResult[i])
            continue
        elif dartResult[i]=='D':
            now=now**2
        elif dartResult[i]=='T':
            now=now**3          
        elif dartResult[i]=='*':
            star=1
        elif dartResult[i]=='#':
            now=now*-1
    
    if star==1:
        answer+=before+now*2
    else:
        answer+=now
        
    return answer