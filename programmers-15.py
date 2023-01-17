def solution(participant, completion): # 완주하지 못한 선수 실패 끝 딕셔너리로 해결
    answer = ''
    par_dict={}
    com_dict={}
    for i in range(len(participant)):
        par_dict[participant[i]]=0
        
        
    for i in range(len(participant)):
        par_dict[participant[i]]=par_dict[participant[i]]+1
            
            
    for i in range(len(completion)):
        par_dict[completion[i]]-=1
             
    for i in range(len(participant)):
        if par_dict[participant[i]]>=1:
            return participant[i]
            
        
    
