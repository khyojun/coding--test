def solution(lottos, win_nums):
    answer = []
    max=0
    min=0
    cnt=0
    cnt_zero=0
    """
    for i in range(len(lottos)):
        if lottos[i]==0:
            cnt_zero+=1
        for j in range(len(win_nums)):
            if lottos[i]==win_nums[j]:
                cnt+=1
     """         
    for x in lottos:
        if x==0:
            cnt_zero+=1
        elif x in win_nums:
            cnt+=1
                
                

    max=7-(cnt_zero+cnt)
    min=7-cnt   
    if max>=6:
        max=6
    
    if min>=6:
        min=6   
    
    answer.append(max)
    answer.append(min)    
       
    return answer
