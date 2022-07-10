new_id=''

answer = ''
#1단계
answer=new_id.lower()
        
#2단계
    
s=list(answer)
print(len(s))
i=0
while i <len(s):
    now=ord(s[i])
    if (now>=ord('a') and now<=ord('z')) or (now == ord('-')) or (now == ord('_')) or (now == ord('.') (now>=ord('1') and now<=ord('9'))):
        i=i+1
        continue
    else:
        del(s[i])
    
#3단계
answer="".join(s)
while '..' in answer:
    answer=answer.replace('..', '.')
    
#4단계
answer=answer.strip('.')
        
#5단계
if not answer:
    answer='a'
        
#6단계
s=list(answer)
if len(s)>=16:
    del(s[15:])  
    if s[14]=='.':
        del(s[14])
    
    
#7단계
while len(s)<=2:
    s.append(s[-1])
    
            
answer="".join(s)
    
print(answer)

