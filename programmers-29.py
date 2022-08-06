def solution(s):
    answer = s 
    if len(s)%2==0:
        return answer[len(s)//2-1:len(s)//2+1]
    else:
         return answer[len(s)//2]
        
   