def solution(rows, columns, queries):
    answer = []
    arr=[]
    cnt=1
    for i in range(rows):
        col=[]
        for j in range(columns):
            col.append(cnt)
            cnt+=1
        arr.append(col)
    
    for i in range(len(queries)):
        x1=queries[i][0]
        y1=queries[i][1]
        x2=queries[i][2]
        y2=queries[i][3]
             
        x_move=x2-x1
        y_move=y2-y1
            
        start_x=x1-1
        start_y=y1-1
            
        end_x=x2-1
        end_y=y2-1
            
        now_x=start_x
        now_y=start_y
        tmp=arr[start_x][start_y]
            
        mini=30000
            
        for j in range(1, y_move+1): # 가로 첫 무빙
            now=tmp
            tmp=arr[now_x][now_y+j]
            arr[now_x][now_y+j]=now
            mini=min(now, mini)
            if (now_y+j)==end_y:
                now_y=now_y+j
                break
                    
        for j in range(1, x_move+1): # 세로 내려가기
            now=tmp
            tmp=arr[now_x+j][now_y]
            arr[now_x+j][now_y]=now          
            mini=min(now, mini)
            if now_x+j==end_x:  
                now_x=now_x+j
                break
                
                    
        for j in range(1, y_move+1): # 역가로 무빙
            now=tmp
            tmp=arr[now_x][now_y-j]
            arr[now_x][now_y-j]=now
            mini=min(now, mini)
            if (now_y-j)==start_y:
                now_y=now_y-j
                break   
            
        for j in range(1, x_move+1): # 세로 올라가기
            now=tmp
            tmp=arr[now_x-j][now_y]
            arr[now_x-j][now_y]=now
            mini=min(now, mini)
            if (now_x-j)==start_x:
                now_x=now_x-j
                break
                    
        answer.append(mini)
            
    return answer
  