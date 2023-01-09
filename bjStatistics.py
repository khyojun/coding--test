import sys
def input(): return sys.stdin.readline().rstrip()  # 이거 안넣어서 계속 시간 초과 뜸 ***** 입력시간을 줄여주는 함수
n=int(input())
a=[]
common=dict()
for i in range(n):
     a.append(int(input()))
     common[a[i]]=0
    

for i in a:
    common[i]=common[i]+1


a.sort()

print(round(sum(a)/n))

print(a[n//2])
max_count_a=0
Mode=[]
max_count_a=max(common.values())

for i in common:
    if max_count_a==common[i]:
        Mode.append(i)


Mode.sort()
if len(Mode)>1:
    print(Mode[1])
else:
    print(Mode[0])

print(max(a)-min(a))



