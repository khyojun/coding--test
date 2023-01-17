def solution(n): # 3진법 뒤집기
    answer = 0
    three=[]
    while True:
        if n<3:
            three.append(n)
            break
        three.append(n%3)
        n=n//3
    
    cnt_three=1
    leng=len(three)
    for i in range(len(three)-1, -1, -1):
        answer+=cnt_three*three[i]
        cnt_three*=3
        
    return answer
    
    
