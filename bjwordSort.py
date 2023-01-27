import sys
def input(): return sys.stdin.readline().rstrip()
n = int(input())
str_lis=[]
length_lis=[]

for i in range(n):
    s=input()
    length_lis.append(len(s))
    str_lis.append(s)

length_lis.sort()
str_lis.sort()

noDuplicated=list(set(str_lis))
noDuplicated_length=list(set(length_lis))
noDuplicated.sort()
noDuplicated_length.sort()
n=len(noDuplicated)
queue=[]
idx=0
while(idx<n):
    if len(queue)>= n:
        break

    for i in range(len(noDuplicated)):
        if noDuplicated_length[idx]==len(noDuplicated[i]):
            queue.append(noDuplicated[i])
    idx+=1

for i in range(len(queue)):
    print(queue[i])






