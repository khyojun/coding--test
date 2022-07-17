def solution(absolutes, signs): # 음양더하기
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    
    
    return answer