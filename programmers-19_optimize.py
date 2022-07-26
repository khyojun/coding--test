def solution(left, right): # 약수의 개수
    answer = 0
    for i in range(left, right+1): # 제곱수는 약수의 갯수가 홀수!
        if int(i**0.5)==i**0.5:
            answer+=i
        else:
            answer-=i
    return answer
