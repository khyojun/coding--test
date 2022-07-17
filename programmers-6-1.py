def solution(board, moves):
    answer = 0
    stack=[]
    cnt=0
    
    while cnt != len(moves):
        much=len(board[moves[cnt]-1])
        now_x=moves[cnt]-1
        for i in range(much):
            if board[i][now_x]==0:
                continue
            else:                   
                tmp=board[i][now_x]
                board[i][now_x]=0
                stack.append(tmp)
                break                        
        cnt+=1 
    

    while True:
        flag=0
        i=0
        while True:
            if i>=len(stack)-1:
                break
            
            if stack[i]==stack[i+1]:
                del(stack[i])
                del(stack[i])
                answer=answer+2
                flag=1
            i+=1
            
        if flag==0:
            break
            
    return answer