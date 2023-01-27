import sys
def input(): return sys.stdin.readline().rstrip()

def solve(delete, parents, child):
    parents[delete]=-1e9
    for i in range(len(child[delete])):
        solve(child[delete][i],parents,child)

def count_child(now_child, parents):
    count=0
    for i in range(len(now_child)):
        if parents[now_child[i]] !=-1e9:
            count+=1
    return count

n=int(input())
parents=list(map(int, input().split()))
delete=int(input())

child= [[] for i in range(len(parents))]

for i in range(len(parents)):
    if parents[i]==-1:
        continue
    child[parents[i]].append(i)

solve(delete, parents,child)
count=0
for i in range(n):
    if count_child(child[i], parents) == 0 and parents[i] !=-1e9:
        count+=1

print(count)