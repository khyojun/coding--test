sol="IOI"
input_str=[]
n=int(input())
size=int(input())

input_str=input()
sol="IOI"
cnt=0
result=0
now_index=0
while(now_index < len(input_str)):
    if input_str[now_index:now_index+3] == "IOI":
        cnt+=1
        now_index+=2
        if cnt==n:
            cnt-=1
            result+=1       
        continue
    now_index+=1
    cnt=0
    

print(result)



