

# k번째 해당하는 b 문자 찾기 

a=input()
k=int(input())

find='b'
count=1
result=-1
for i in range(len(a)):
    if a[i]==find and count==k:
        print(i)
        break
    elif a[i]==find and count!=k:
        count+=1

if result==-1:
    print("None")
else:
    print(result)





