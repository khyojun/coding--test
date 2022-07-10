def solution(record): # 오픈채팅방 카카오 Blind Recruit
    answer = []
    di={}
    for i in range(len(record)):
        tmp= record[i].split()
        if tmp[0]=='Enter':
            di[tmp[1]]=tmp[2]
        elif tmp[0]=='Change':
            di[tmp[1]]=tmp[2]
    
    #출력
    for i in range(len(record)):
        tmp=record[i].split()
        if tmp[0]=='Enter':
            answer.append(di[tmp[1]]+'님이 들어왔습니다.')
        elif tmp[0]=='Leave':
            answer.append(di[tmp[1]]+'님이 나갔습니다.')
    
    
    return answer