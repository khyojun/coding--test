def solution(n): # 나머지가 1이 되는 수 찾기
    answer = 0
    for i in range(2, n):
        if n%i==1:
            return i