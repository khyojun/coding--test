from itertools import combinations # 소수 만들기

def is_prime(m):
    
    for i in range(2, int(m**0.5)+1):
        if m%i==0:
            return False
    return True


def solution(nums):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    com=combinations(nums, 3)
    for i in com:
        now_list=list(i)
        sum=0
        for j in now_list:
            sum+=j
        if is_prime(sum):
            answer+=1
        

    return answer