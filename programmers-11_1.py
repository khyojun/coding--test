def solution(answers):
    answer = []
    num1=[1,2,3,4,5]
    num2=[2,1,2,3,2,4,2,5]
    num3=[3,3,1,1,2,2,4,4,5,5]
    maxi=0
    cnt_1=0
    cnt_2=0
    cnt_3=0
    
    
    for i in range(len(answers)):
        if num1[i%len(num1)]==answers[i]:
            cnt_1+=1
        if num2[i%len(num2)]==answers[i]:
            cnt_2+=1
        if num3[i%len(num3)]==answers[i]:
            cnt_3+=1
        maxi=max(cnt_1, cnt_2, cnt_3)
    
    if maxi==cnt_1:
        answer.append(1)
    
    if maxi==cnt_2:
        answer.append(2)
    
    if maxi==cnt_3:
        answer.append(3)
    
    return answer