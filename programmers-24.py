def solution(numbers): # 두 개 뽑아서 더하기
    answer = []
    tmp=0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])   
    answer_set=set(answer)
    answer=list(answer_set)
    answer.sort()
    return answer