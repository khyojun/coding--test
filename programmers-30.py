def bina(n,cnt): # 비밀지도
    bina=[]
    while(cnt):
        if n==0:
            bina.append(0)
            cnt-=1
            continue
        bina.append(n%2)
        n=n//2
        cnt-=1
    bina.reverse()
    return bina
        
    


def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        str_map=[]
        a=[]
        b=[]
        a=bina(arr1[i],n)
        b=bina(arr2[i],n)
        for j in range(n):
            if a[j] or b[j]:   
                str_map.append('#')
            else:
                str_map.append(' ')
                  
        ans_str=''.join(str_map)
        answer.append(ans_str)
    
        
        
    
    
    return answer