def solution(numbers): # 없는 숫자 더하기
    answer = -1
    answer=0
    for i in range(0, 10):
        if not i in numbers:
            answer+=i
    
    return answer